package com.ait.quiz.model;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Encapsulates the results of a single quiz attempt by a student.
 * Keeps track of score, grading, and detailed question breakdown.
 */
public class QuizAttempt {

    private final String attemptId;
    private final String quizId;
    private final String quizTitle;
    private final String studentRollNumber;
    private final String studentName;
    private final String timestamp;

    private int totalQuestions;
    private int correctCount;
    private int incorrectCount;
    private double scoreObtained;
    private int totalPossibleMarks;
    private double percentage;
    private String grade;

    // Detailed record of each question result
    public static class QuestionResult {
        private final int questionId;
        private final String questionText;
        private final String studentAnswer;
        private final String correctAnswer;
        private final boolean isCorrect;
        private final double marksAwarded;

        public QuestionResult(int questionId, String questionText, String studentAnswer, 
                              String correctAnswer, boolean isCorrect, double marksAwarded) {
            this.questionId = questionId;
            this.questionText = questionText;
            this.studentAnswer = studentAnswer;
            this.correctAnswer = correctAnswer;
            this.isCorrect = isCorrect;
            this.marksAwarded = marksAwarded;
        }

        public int getQuestionId() { return questionId; }
        public String getQuestionText() { return questionText; }
        public String getStudentAnswer() { return studentAnswer; }
        public String getCorrectAnswer() { return correctAnswer; }
        public boolean isCorrect() { return isCorrect; }
        public double getMarksAwarded() { return marksAwarded; }
    }

    private final List<QuestionResult> questionResults = new ArrayList<>();

    public QuizAttempt(String attemptId, String quizId, String quizTitle, String studentRollNumber, String studentName) {
        this.attemptId = attemptId;
        this.quizId = quizId;
        this.quizTitle = quizTitle;
        this.studentRollNumber = studentRollNumber;
        this.studentName = studentName;
        this.timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("dd-MMM-yyyy HH:mm:ss"));
    }

    public void addQuestionResult(QuestionResult result) {
        questionResults.add(result);
    }

    public List<QuestionResult> getQuestionResults() {
        return Collections.unmodifiableList(questionResults);
    }

    public String getAttemptId() { return attemptId; }
    public String getQuizId() { return quizId; }
    public String getQuizTitle() { return quizTitle; }
    public String getStudentRollNumber() { return studentRollNumber; }
    public String getStudentName() { return studentName; }
    public String getTimestamp() { return timestamp; }

    public int getTotalQuestions() { return totalQuestions; }
    public void setTotalQuestions(int totalQuestions) { this.totalQuestions = totalQuestions; }

    public int getCorrectCount() { return correctCount; }
    public void setCorrectCount(int correctCount) { this.correctCount = correctCount; }

    public int getIncorrectCount() { return incorrectCount; }
    public void setIncorrectCount(int incorrectCount) { this.incorrectCount = incorrectCount; }

    public double getScoreObtained() { return scoreObtained; }
    public void setScoreObtained(double scoreObtained) { this.scoreObtained = scoreObtained; }

    public int getTotalPossibleMarks() { return totalPossibleMarks; }
    public void setTotalPossibleMarks(int totalPossibleMarks) { this.totalPossibleMarks = totalPossibleMarks; }

    public double getPercentage() { return percentage; }
    public void setPercentage(double percentage) { this.percentage = percentage; }

    public String getGrade() { return grade; }
    public void setGrade(String grade) { this.grade = grade; }

    @Override
    public String toString() {
        return String.format("[%s] Student: %s (%s) | Quiz: %s | Score: %.2f/%d (%.2f%%) | Grade: %s",
                attemptId, studentName, studentRollNumber, quizId, scoreObtained, totalPossibleMarks, percentage, grade);
    }
}
