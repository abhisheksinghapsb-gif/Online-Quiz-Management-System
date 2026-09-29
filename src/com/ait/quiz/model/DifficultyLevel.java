package com.ait.quiz.model;

/**
 * Enumeration representing the difficulty level of a quiz question or quiz.
 */
public enum DifficultyLevel {
    EASY("Easy"),
    MEDIUM("Medium"),
    HARD("Hard");

    private final String displayName;

    DifficultyLevel(String displayName) {
        this.displayName = displayName;
    }

    public String getDisplayName() {
        return displayName;
    }

    public static DifficultyLevel fromString(String text) {
        for (DifficultyLevel level : DifficultyLevel.values()) {
            if (level.name().equalsIgnoreCase(text) || level.displayName.equalsIgnoreCase(text)) {
                return level;
            }
        }
        return MEDIUM; // Default fallback
    }
}
