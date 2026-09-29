package com.ait.quiz.web;

import com.ait.quiz.exception.*;
import com.ait.quiz.main.QuizApplication;
import com.ait.quiz.model.*;
import com.ait.quiz.service.*;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

/**
 * Embedded lightweight HTTP Web Server for the Online Quiz Management System.
 * Connects the Java backend models, services, and exception hierarchy to a modern web browser UI.
 * Runs on standard Java SE without third-party frameworks.
 */
public class QuizWebServer {

    private static final int DEFAULT_PORT = 8080;
    private final QuizOperations quizManager;
    private final Path staticDir;
    private HttpServer server;

    public QuizWebServer(QuizOperations quizManager, Path staticDir) {
        this.quizManager = quizManager;
        this.staticDir = staticDir;
    }

    public static void main(String[] args) {
        int port = DEFAULT_PORT;
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException ignored) {}
        }

        Path webPath = Paths.get("web");
        if (!Files.exists(webPath)) {
            webPath = Paths.get("../web");
        }

        QuizOperations manager = new QuizManager();
        QuizWebServer webServer = new QuizWebServer(manager, webPath.toAbsolutePath().normalize());

        try {
            webServer.start(port);
            System.out.println("================================================================================");
            System.out.println("           ONLINE QUIZ MANAGEMENT SYSTEM - WEB SERVER STARTED           ");
            System.out.println("================================================================================");
            System.out.println(" Server URL  : http://localhost:" + port);
            System.out.println(" Static Dir  : " + webPath.toAbsolutePath().normalize());
            System.out.println(" Status      : Ready to accept requests from web browser");
            System.out.println(" Press Ctrl+C in this console to stop the server.");
            System.out.println("================================================================================");
        } catch (IOException e) {
            System.err.println("Failed to start web server on port " + port + ": " + e.getMessage());
        }
    }

    public void start(int port) throws IOException {
        server = HttpServer.create(new InetSocketAddress(port), 0);

        // API Endpoints
        server.createContext("/api/quizzes", new QuizzesHandler());
        server.createContext("/api/submit", new SubmitQuizHandler());
        server.createContext("/api/attempts", new AttemptsHandler());
        server.createContext("/api/demo", new DemoRunnerHandler());

        // Static Web Content Handler
        server.createContext("/", new StaticFileHandler(staticDir));

        server.setExecutor(java.util.concurrent.Executors.newCachedThreadPool());
        server.start();
    }

    public void stop() {
        if (server != null) {
            server.stop(0);
        }
    }

    // =========================================================================
    // API HANDLERS
    // =========================================================================

    private class QuizzesHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            String method = exchange.getRequestMethod().toUpperCase();

            if (method.equals("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            if (method.equals("GET")) {
                List<Quiz> quizzes = quizManager.getAllQuizzes();
                StringBuilder json = new StringBuilder("[");
                for (int i = 0; i < quizzes.size(); i++) {
                    Quiz q = quizzes.get(i);
                    json.append("{");
                    json.append("\"quizId\":").append(quote(q.getQuizId())).append(",");
                    json.append("\"title\":").append(quote(q.getTitle())).append(",");
                    json.append("\"description\":").append(quote(q.getDescription())).append(",");
                    json.append("\"topic\":").append(quote(q.getTopic())).append(",");
                    json.append("\"difficulty\":").append(quote(q.getDifficulty().getDisplayName())).append(",");
                    json.append("\"targetAgeGroup\":").append(quote(q.getTargetAgeGroup())).append(",");
                    json.append("\"totalMarks\":").append(q.getTotalMarks()).append(",");
                    json.append("\"questionCount\":").append(q.getQuestionCount()).append(",");
                    json.append("\"questions\":[");
                    List<Question> questions = q.getQuestions();
                    for (int j = 0; j < questions.size(); j++) {
                        Question que = questions.get(j);
                        json.append("{");
                        json.append("\"id\":").append(que.getId()).append(",");
                        json.append("\"questionText\":").append(quote(que.getQuestionText())).append(",");
                        json.append("\"marks\":").append(que.getMarks()).append(",");
                        json.append("\"topic\":").append(quote(que.getTopic())).append(",");
                        json.append("\"difficulty\":").append(quote(que.getDifficulty().getDisplayName())).append(",");
                        json.append("\"type\":").append(quote(que.getQuestionType())).append(",");
                        if (que instanceof MultipleChoiceQuestion) {
                            MultipleChoiceQuestion mcq = (MultipleChoiceQuestion) que;
                            json.append("\"options\":[");
                            List<String> opts = mcq.getOptions();
                            for (int k = 0; k < opts.size(); k++) {
                                json.append(quote(opts.get(k)));
                                if (k < opts.size() - 1) json.append(",");
                            }
                            json.append("]");
                        } else {
                            json.append("\"options\":[]");
                        }
                        json.append("}");
                        if (j < questions.size() - 1) json.append(",");
                    }
                    json.append("]");
                    json.append("}");
                    if (i < quizzes.size() - 1) json.append(",");
                }
                json.append("]");

                sendJsonResponse(exchange, 200, json.toString());
            } else if (method.equals("POST")) {
                // Create a new quiz
                String body = readRequestBody(exchange);
                try {
                    Map<String, String> params = parseSimpleJson(body);
                    String id = params.get("quizId");
                    String title = params.get("title");
                    String desc = params.get("description");
                    String topic = params.get("topic");
                    String diff = params.get("difficulty");
                    String ageGroup = params.get("targetAgeGroup");

                    DifficultyLevel level = DifficultyLevel.fromString(diff);
                    Quiz newQuiz = new Quiz(id, title, desc, topic, level, (ageGroup != null ? ageGroup : "College (18-22)"));
                    quizManager.createQuiz(newQuiz);

                    sendJsonResponse(exchange, 201, "{\"success\":true,\"message\":\"Quiz created successfully!\"}");
                } catch (DuplicateQuizException dqe) {
                    sendJsonResponse(exchange, 400, "{\"success\":false,\"error\":" + quote(dqe.getMessage()) + "}");
                } catch (Exception e) {
                    sendJsonResponse(exchange, 500, "{\"success\":false,\"error\":" + quote(e.getMessage()) + "}");
                }
            } else {
                exchange.sendResponseHeaders(405, -1);
            }
        }
    }

    private class SubmitQuizHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if (exchange.getRequestMethod().equalsIgnoreCase("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            if (!exchange.getRequestMethod().equalsIgnoreCase("POST")) {
                exchange.sendResponseHeaders(405, -1);
                return;
            }

            String body = readRequestBody(exchange);
            try {
                // Parse submission JSON
                // Example payload: { "quizId": "JAVA-OOP", "studentName": "...", "rollNumber": "...", "policy": "competitive", "answers": { "1": "B", "2": "A" } }
                Map<String, String> root = parseSimpleJson(body);
                String quizId = root.get("quizId");
                String studentName = root.getOrDefault("studentName", "Student");
                String rollNumber = root.getOrDefault("rollNumber", "3101");
                String policy = root.getOrDefault("policy", "standard");

                Quiz quiz = quizManager.getQuiz(quizId);
                quiz.validateForConduct();

                // Select evaluation strategy (Interface Polymorphism)
                QuizEvaluator evaluator = policy.equalsIgnoreCase("competitive")
                        ? new NegativeMarkingGradingPolicy(0.25)
                        : new StandardGradingPolicy();

                String attemptId = "ATT-" + UUID.randomUUID().toString().substring(0, 6).toUpperCase();
                QuizAttempt attempt = new QuizAttempt(attemptId, quiz.getQuizId(), quiz.getTitle(), rollNumber, studentName);
                attempt.setTotalQuestions(quiz.getQuestionCount());
                attempt.setTotalPossibleMarks(quiz.getTotalMarks());

                Map<String, String> answers = extractNestedMap(body, "answers");

                int correctCount = 0;
                int incorrectCount = 0;

                for (Question q : quiz.getQuestions()) {
                    String studentAns = answers.getOrDefault(String.valueOf(q.getId()), "").trim();
                    boolean isCorrect = false;
                    try {
                        isCorrect = q.checkAnswer(studentAns);
                    } catch (InvalidOptionException ioe) {
                        isCorrect = false;
                    }

                    double marks = isCorrect ? q.getMarks() : 0.0;
                    if (isCorrect) correctCount++;
                    else incorrectCount++;

                    attempt.addQuestionResult(new QuizAttempt.QuestionResult(
                            q.getId(),
                            q.getQuestionText(),
                            studentAns.isEmpty() ? "(Unanswered)" : studentAns,
                            q.getCorrectAnswerFormatted(),
                            isCorrect,
                            marks
                    ));
                }

                attempt.setCorrectCount(correctCount);
                attempt.setIncorrectCount(incorrectCount);

                double score = evaluator.evaluateScore(attempt);
                attempt.setScoreObtained(score);
                double percentage = (quiz.getTotalMarks() > 0) ? (score / quiz.getTotalMarks()) * 100.0 : 0.0;
                attempt.setPercentage(percentage);
                attempt.setGrade(evaluator.generateGrade(percentage));

                quizManager.recordAttempt(attempt);

                // Build detailed response JSON
                StringBuilder json = new StringBuilder("{");
                json.append("\"success\":true,");
                json.append("\"attemptId\":").append(quote(attempt.getAttemptId())).append(",");
                json.append("\"quizTitle\":").append(quote(attempt.getQuizTitle())).append(",");
                json.append("\"studentName\":").append(quote(attempt.getStudentName())).append(",");
                json.append("\"rollNumber\":").append(quote(attempt.getStudentRollNumber())).append(",");
                json.append("\"policyName\":").append(quote(evaluator.getPolicyName())).append(",");
                json.append("\"timestamp\":").append(quote(attempt.getTimestamp())).append(",");
                json.append("\"totalQuestions\":").append(attempt.getTotalQuestions()).append(",");
                json.append("\"correctCount\":").append(attempt.getCorrectCount()).append(",");
                json.append("\"incorrectCount\":").append(attempt.getIncorrectCount()).append(",");
                json.append("\"scoreObtained\":").append(String.format(Locale.US, "%.2f", attempt.getScoreObtained())).append(",");
                json.append("\"totalPossibleMarks\":").append(attempt.getTotalPossibleMarks()).append(",");
                json.append("\"percentage\":").append(String.format(Locale.US, "%.2f", attempt.getPercentage())).append(",");
                json.append("\"grade\":").append(quote(attempt.getGrade())).append(",");
                json.append("\"results\":[");
                List<QuizAttempt.QuestionResult> list = attempt.getQuestionResults();
                for (int i = 0; i < list.size(); i++) {
                    QuizAttempt.QuestionResult qr = list.get(i);
                    json.append("{");
                    json.append("\"questionId\":").append(qr.getQuestionId()).append(",");
                    json.append("\"questionText\":").append(quote(qr.getQuestionText())).append(",");
                    json.append("\"studentAnswer\":").append(quote(qr.getStudentAnswer())).append(",");
                    json.append("\"correctAnswer\":").append(quote(qr.getCorrectAnswer())).append(",");
                    json.append("\"isCorrect\":").append(qr.isCorrect()).append(",");
                    json.append("\"marksAwarded\":").append(qr.getMarksAwarded());
                    json.append("}");
                    if (i < list.size() - 1) json.append(",");
                }
                json.append("]");
                json.append("}");

                sendJsonResponse(exchange, 200, json.toString());
            } catch (Exception e) {
                sendJsonResponse(exchange, 400, "{\"success\":false,\"error\":" + quote(e.getMessage()) + "}");
            }
        }
    }

    private class AttemptsHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if (exchange.getRequestMethod().equalsIgnoreCase("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            List<QuizAttempt> attempts = quizManager.getAllAttempts();
            StringBuilder json = new StringBuilder("[");
            for (int i = 0; i < attempts.size(); i++) {
                QuizAttempt a = attempts.get(i);
                json.append("{");
                json.append("\"attemptId\":").append(quote(a.getAttemptId())).append(",");
                json.append("\"quizId\":").append(quote(a.getQuizId())).append(",");
                json.append("\"quizTitle\":").append(quote(a.getQuizTitle())).append(",");
                json.append("\"studentName\":").append(quote(a.getStudentName())).append(",");
                json.append("\"rollNumber\":").append(quote(a.getStudentRollNumber())).append(",");
                json.append("\"scoreObtained\":").append(String.format(Locale.US, "%.2f", a.getScoreObtained())).append(",");
                json.append("\"totalPossibleMarks\":").append(a.getTotalPossibleMarks()).append(",");
                json.append("\"percentage\":").append(String.format(Locale.US, "%.2f", a.getPercentage())).append(",");
                json.append("\"grade\":").append(quote(a.getGrade())).append(",");
                json.append("\"timestamp\":").append(quote(a.getTimestamp()));
                json.append("}");
                if (i < attempts.size() - 1) json.append(",");
            }
            json.append("]");

            sendJsonResponse(exchange, 200, json.toString());
        }
    }

    private class DemoRunnerHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if (exchange.getRequestMethod().equalsIgnoreCase("OPTIONS")) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            // Capture output of the demonstration suite
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            PrintStream origOut = System.out;
            PrintStream origErr = System.err;
            try {
                PrintStream ps = new PrintStream(baos);
                System.setOut(ps);
                System.setErr(ps);

                QuizApplication app = new QuizApplication();
                // Run automated test suite logic
                app.runAutomatedDemonstrationSuite();
            } finally {
                System.setOut(origOut);
                System.setErr(origErr);
            }

            String trace = baos.toString(StandardCharsets.UTF_8);
            sendJsonResponse(exchange, 200, "{\"success\":true,\"trace\":" + quote(trace) + "}");
        }
    }

    // =========================================================================
    // STATIC FILE SERVING
    // =========================================================================

    private static class StaticFileHandler implements HttpHandler {
        private final Path rootDir;

        public StaticFileHandler(Path rootDir) {
            this.rootDir = rootDir;
        }

        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String pathStr = exchange.getRequestURI().getPath();
            if (pathStr == null || pathStr.equals("/") || pathStr.isEmpty()) {
                pathStr = "/index.html";
            }

            // Prevent path traversal
            Path resolved = rootDir.resolve(pathStr.substring(1)).normalize();
            if (!resolved.startsWith(rootDir) || !Files.exists(resolved) || Files.isDirectory(resolved)) {
                String notFound = "<h1>404 Not Found</h1><p>The requested file was not found.</p>";
                exchange.sendResponseHeaders(404, notFound.length());
                OutputStream os = exchange.getResponseBody();
                os.write(notFound.getBytes(StandardCharsets.UTF_8));
                os.close();
                return;
            }

            String contentType = getMimeType(resolved.toString());
            exchange.getResponseHeaders().set("Content-Type", contentType);
            byte[] bytes = Files.readAllBytes(resolved);
            exchange.sendResponseHeaders(200, bytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(bytes);
            os.close();
        }

        private String getMimeType(String file) {
            if (file.endsWith(".html") || file.endsWith(".htm")) return "text/html; charset=utf-8";
            if (file.endsWith(".css")) return "text/css; charset=utf-8";
            if (file.endsWith(".js")) return "application/javascript; charset=utf-8";
            if (file.endsWith(".json")) return "application/json; charset=utf-8";
            if (file.endsWith(".png")) return "image/png";
            if (file.endsWith(".jpg") || file.endsWith(".jpeg")) return "image/jpeg";
            if (file.endsWith(".svg")) return "image/svg+xml";
            return "text/plain; charset=utf-8";
        }
    }

    // =========================================================================
    // HELPERS
    // =========================================================================

    private static void addCorsHeaders(HttpExchange exchange) {
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE");
        exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type, Authorization");
    }

    private static void sendJsonResponse(HttpExchange exchange, int status, String json) throws IOException {
        byte[] bytes = json.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json; charset=utf-8");
        exchange.sendResponseHeaders(status, bytes.length);
        OutputStream os = exchange.getResponseBody();
        os.write(bytes);
        os.close();
    }

    private static String readRequestBody(HttpExchange exchange) throws IOException {
        InputStream is = exchange.getRequestBody();
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        byte[] buffer = new byte[1024];
        int len;
        while ((len = is.read(buffer)) != -1) {
            baos.write(buffer, 0, len);
        }
        return baos.toString(StandardCharsets.UTF_8);
    }

    private static String quote(String str) {
        if (str == null) return "\"\"";
        StringBuilder sb = new StringBuilder("\"");
        for (char c : str.toCharArray()) {
            switch (c) {
                case '"': sb.append("\\\""); break;
                case '\\': sb.append("\\\\"); break;
                case '\b': sb.append("\\b"); break;
                case '\f': sb.append("\\f"); break;
                case '\n': sb.append("\\n"); break;
                case '\r': sb.append("\\r"); break;
                case '\t': sb.append("\\t"); break;
                default:
                    if (c < ' ') {
                        sb.append(String.format("\\u%04x", (int) c));
                    } else {
                        sb.append(c);
                    }
            }
        }
        sb.append("\"");
        return sb.toString();
    }

    private static Map<String, String> parseSimpleJson(String json) {
        Map<String, String> map = new HashMap<>();
        if (json == null || json.trim().isEmpty()) return map;

        String trimmed = json.trim();
        if (trimmed.startsWith("{")) trimmed = trimmed.substring(1);
        if (trimmed.endsWith("}")) trimmed = trimmed.substring(0, trimmed.length() - 1);

        String[] pairs = trimmed.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
        for (String pair : pairs) {
            String[] kv = pair.split(":(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", 2);
            if (kv.length == 2) {
                String key = cleanQuotes(kv[0].trim());
                String val = cleanQuotes(kv[1].trim());
                map.put(key, val);
            }
        }
        return map;
    }

    private static Map<String, String> extractNestedMap(String json, String parentKey) {
        Map<String, String> result = new HashMap<>();
        int keyIndex = json.indexOf("\"" + parentKey + "\"");
        if (keyIndex == -1) return result;

        int openBrace = json.indexOf("{", keyIndex);
        if (openBrace == -1) return result;

        int closeBrace = json.indexOf("}", openBrace);
        if (closeBrace == -1) return result;

        String inner = json.substring(openBrace + 1, closeBrace);
        String[] pairs = inner.split(",");
        for (String p : pairs) {
            String[] kv = p.split(":");
            if (kv.length == 2) {
                result.put(cleanQuotes(kv[0].trim()), cleanQuotes(kv[1].trim()));
            }
        }
        return result;
    }

    private static String cleanQuotes(String s) {
        if (s.startsWith("\"") && s.endsWith("\"") && s.length() >= 2) {
            return s.substring(1, s.length() - 1);
        }
        return s;
    }
}
