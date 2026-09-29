package com.ait.quiz.model;

/**
 * Abstract class representing a System User.
 * Demonstrates:
 * - Abstract class with common user state and abstract dashboard presentation.
 */
public abstract class User {

    private final String userId;
    private String name;
    private String email;

    public User(String userId, String name, String email) {
        if (userId == null || userId.trim().isEmpty()) {
            throw new IllegalArgumentException("User ID cannot be empty!");
        }
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty!");
        }
        this.userId = userId.trim();
        this.name = name.trim();
        this.email = (email != null && !email.trim().isEmpty()) ? email.trim() : "user@aitpune.edu.in";
    }

    public String getUserId() {
        return userId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * Abstract method to be implemented polymorphically depending on user role.
     */
    public abstract void displayDashboard();

    /**
     * Returns user role (e.g., "Student", "Instructor").
     */
    public abstract String getRole();

    @Override
    public String toString() {
        return String.format("[%s] ID: %s | Name: %s (%s)", getRole(), userId, name, email);
    }
}
