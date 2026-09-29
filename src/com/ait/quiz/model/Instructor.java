package com.ait.quiz.model;

/**
 * Concrete class representing an Instructor / Faculty member.
 * Demonstrates:
 * - Inheritance (extends User)
 * - Method Overriding (displayDashboard, getRole)
 */
public class Instructor extends User {

    private final String department;
    private final String designation;

    public Instructor(String userId, String name, String email, String department, String designation) {
        super(userId, name, email);
        this.department = (department != null) ? department : "Information Technology";
        this.designation = (designation != null) ? designation : "Assistant Professor";
    }

    public String getDepartment() {
        return department;
    }

    public String getDesignation() {
        return designation;
    }

    @Override
    public void displayDashboard() {
        System.out.println("==================================================");
        System.out.println("          INSTRUCTOR / FACULTY DASHBOARD          ");
        System.out.println("==================================================");
        System.out.printf("Faculty Name: %s%n", getName());
        System.out.printf("Designation : %s%n", designation);
        System.out.printf("Department  : %s%n", department);
        System.out.printf("Email       : %s%n", getEmail());
        System.out.println("Authorized Actions: Create Quizzes, Add Questions, View Reports");
        System.out.println("--------------------------------------------------");
    }

    @Override
    public String getRole() {
        return "Instructor";
    }
}
