package com.ait.quiz.service;

import com.ait.quiz.model.QuizAttempt;

/**
 * Competitive exam grading implementation of QuizEvaluator.
 * Penalizes incorrect answers with a configurable negative deduction factor (default 25% penalty).
 * Demonstrates:
 * - Interface Implementation
 * - Polymorphism (Method Overriding & Overloading)
 */
public class NegativeMarkingGradingPolicy implements QuizEvaluator {

    private final double penaltyRate; // e.g. 0.25 for 25% negative marking

    public NegativeMarkingGradingPolicy() {
        this(0.25);
    }

    public NegativeMarkingGradingPolicy(double penaltyRate) {
        if (penaltyRate < 0.0 || penaltyRate > 1.0) {
            throw new IllegalArgumentException("Penalty rate must be between 0.0 and 1.0!");
        }
        this.penaltyRate = penaltyRate;
    }

    public double getPenaltyRate() {
        return penaltyRate;
    }

    @Override
    public double evaluateScore(QuizAttempt attempt) {
        double rawScore = 0.0;
        for (QuizAttempt.QuestionResult res : attempt.getQuestionResults()) {
            if (res.isCorrect()) {
                rawScore += res.getMarksAwarded();
            } else {
                // Deduct penalty based on question's marks
                double penalty = res.getMarksAwarded() * penaltyRate;
                rawScore -= penalty;
            }
        }
        // Score can be negative or floored at 0 depending on evaluation rules
        return Math.max(0.0, rawScore);
    }

    @Override
    public double evaluateScore(double earnedMarks, int incorrectCount, double penaltyPerIncorrect) {
        double total = earnedMarks - (incorrectCount * penaltyPerIncorrect);
        return Math.max(0.0, total);
    }

    @Override
    public String generateGrade(double percentage) {
        if (percentage >= 85.0) return "O (Exceptional - Competitive Rank 1)";
        if (percentage >= 75.0) return "A+ (Excellent - Advanced Proficiency)";
        if (percentage >= 65.0) return "A (Very Good - High Proficiency)";
        if (percentage >= 50.0) return "B (Qualified)";
        return "Not Qualified (Below cutoff with negative penalties)";
    }

    @Override
    public String getPolicyName() {
        return String.format("Competitive Evaluation (%.0f%% Negative Penalty for wrong answers)", penaltyRate * 100);
    }

    @Override
    public void printDetailedReport(QuizAttempt attempt) {
        System.out.println("================================================================================");
        System.out.println("                 COMPETITIVE EXAM DETAILED SCORECARD WITH PENALTY               ");
        System.out.println("================================================================================");
        System.out.printf("Attempt ID   : %s%n", attempt.getAttemptId());
        System.out.printf("Student Name : %s (Roll No: %s)%n", attempt.getStudentName(), attempt.getStudentRollNumber());
        System.out.printf("Quiz Title   : %s (ID: %s)%n", attempt.getQuizTitle(), attempt.getQuizId());
        System.out.printf("Grading Rule : %s%n", getPolicyName());
        System.out.printf("Date & Time  : %s%n", attempt.getTimestamp());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.printf("Total Questions : %d%n", attempt.getTotalQuestions());
        System.out.printf("Correct Answers : %d%n", attempt.getCorrectCount());
        System.out.printf("Wrong Answers   : %d (-%.0f%% marks penalized per wrong answer)%n", 
                attempt.getIncorrectCount(), penaltyRate * 100);
        System.out.printf("Net Score       : %.2f / %d marks%n", attempt.getScoreObtained(), attempt.getTotalPossibleMarks());
        System.out.printf("Net Percentage  : %.2f%%%n", attempt.getPercentage());
        System.out.printf("Result Status   : %s%n", attempt.getGrade());
        System.out.println("--------------------------------------------------------------------------------");
        System.out.println("ITEM-BY-ITEM AUDIT:");
        int idx = 1;
        for (QuizAttempt.QuestionResult q : attempt.getQuestionResults()) {
            if (q.isCorrect()) {
                System.out.printf(" %2d. [+%.2f marks] %s%n", idx++, q.getMarksAwarded(), q.getQuestionText());
            } else {
                double penalty = q.getMarksAwarded() * penaltyRate;
                System.out.printf(" %2d. [-%.2f PENALTY] %s%n", idx++, penalty, q.getQuestionText());
            }
            System.out.printf("     Your Answer   : %s%n", q.getStudentAnswer());
            System.out.printf("     Correct Answer: %s%n", q.getCorrectAnswer());
        }
        System.out.println("================================================================================");
    }
}
