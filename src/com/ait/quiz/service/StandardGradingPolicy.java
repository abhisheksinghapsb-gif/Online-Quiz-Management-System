package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

/**
 * Standard university grading implementation of QuizEvaluator.
 * Awards full marks for correct answers and zero deduction for incorrect answers.
 * Demonstrates:
 * - Interface Implementation
 * - Polymorphism (Method Overriding & Overloading)
 */
public class StandardGradingPolicy implements QuizEvaluator {

    @Override
    public double evaluateScore(QuizAttempt attempt) {
        double total = 0.0;
        for (QuizAttempt.QuestionResult res : attempt.getQuestionResults()) {
            if (res.isCorrect()) {
                total += res.getMarksAwarded();
            }
        }
        return total;
    }

    @Override
    public double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect) {
        // Standard policy ignores penalty
        return Math.max(0.0, earnedMarks);
    }

    @Override
    public String generateGrade(double percentage) {
        if (percentage >= 90.0) return "O (Outstanding)";
        if (percentage >= 80.0) return "A+ (Excellent)";
        if (percentage >= 70.0) return "A (Very Good)";
        if (percentage >= 60.0) return "B+ (Good)";
        if (percentage >= 50.0) return "B (Above Average)";
        if (percentage >= 40.0) return "C (Pass)";
        return "F (Fail)";
    }

    @Override
    public String getPolicyName() {
        return "Standard Linear Evaluation (No Negative Marking)";
    }

    @Override
    public void printDetailedReport(QuizAttempt attempt) {
        System.out.println("================================================================================");
        System.out.println("                         DETAILED QUIZ PERFORMANCE REPORT                       ");
        System.out.println("================================================================================");
        System.out.printf("Attempt ID   : %s%n", attempt.getAttemptId());
        System.out.printf("Student Name : %s (Roll No: %s)%n", attempt.getStudentName(), attempt.getStudentRollNumber());
        System.out.printf("Quiz Title   : %s (ID: %s)%n", attempt.getQuizTitle(), attempt.getQuizId());
        System.out.printf("Grading Rule : %s%n", getPolicyName());
        System.out.printf("Date & Time  : %s%n", attempt.getTimestamp());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.printf("Total Questions: %d | Correct: %d | Incorrect: %d%n",
                attempt.getTotalQuestions(), attempt.getCorrectCount(), attempt.getIncorrectCount());
        System.out.printf("Final Score    : %.2f / %d marks%n", attempt.getScoreObtained(), attempt.getTotalPossibleMarks());
        System.out.printf("Percentage     : %.2f%%%n", attempt.getPercentage());
        System.out.printf("Awarded Grade  : %s%n", attempt.getGrade());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.println("QUESTION BREAKDOWN:");
        int idx = 1;
        for (QuizAttempt.QuestionResult q : attempt.getQuestionResults()) {
            String status = q.isCorrect() ? "[PASS / CORRECT]" : "[FAIL / INCORRECT]";
            System.out.printf(" %2d. %s %s%n", idx++, status, q.getQuestionText());
            System.out.printf("     Your Answer   : %s%n", q.getStudentAnswer());
            System.out.printf("     Correct Answer: %s%n", q.getCorrectAnswer());
            System.out.printf("     Marks Earned  : %.2f%n", q.getMarksAwarded());
        }
        System.out.println("================================================================================");
    }
}
