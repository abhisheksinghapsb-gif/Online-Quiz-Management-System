package com.ait.quiz.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Concrete class representing a Student user in the Quiz System.
 * Demonstrates:
 * - Inheritance (extends User)
 * - Method Overriding (displayDashboard, getRole)
 * - State management for quiz attempts
 */
public class Student extends User {

    private final String rollNumber;
    private final String division; // e.g. "SE IT A"
    private final List<QuizAttempt> attempts;

    public Student(String userId, String name, String email, String rollNumber, String division) {
        super(userId, name, email);
        this.rollNumber = rollNumber;
        this.division = (division != null) ? division : "SE IT";
        this.attempts = new ArrayList<>();
    }

    public String getRollNumber() {
        return rollNumber;
    }

    public String getDivision() {
        return division;
    }

    public void addAttempt(QuizAttempt attempt) {
        if (attempt != null) {
            attempts.add(attempt);
        }
    }

    public List<QuizAttempt> getAttempts() {
        return Collections.unmodifiableList(attempts);
    }

    public double getAveragePercentage() {
        if (attempts.isEmpty()) return 0.0;
        double sum = 0;
        for (QuizAttempt att : attempts) {
            sum += att.getPercentage();
        }
        return sum / attempts.size();
    }

    @Override
    public void displayDashboard() {
        System.out.println("==================================================");
        System.out.println("           STUDENT PORTAL DASHBOARD               ");
        System.out.println("==================================================");
        System.out.printf("Name       : %s%n", getName());
        System.out.printf("Roll No    : %s | Division: %s%n", rollNumber, division);
        System.out.printf("Email      : %s%n", getEmail());
        System.out.printf("Total Quizzes Attempted : %d%n", attempts.size());
        if (!attempts.isEmpty()) {
            System.out.printf("Average Score           : %.2f%%%n", getAveragePercentage());
        }
        System.out.println("--------------------------------------------------");
    }

    @Override
    public String getRole() {
        return "Student";
    }
}
