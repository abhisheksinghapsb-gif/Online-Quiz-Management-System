package com.ait.quiz.model;

import com.ait.quiz.exception.EmptyQuizException;
import com.ait.quiz.exception.InvalidQuestionException;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Represents a Quiz composed of polymorphic Question objects.
 * Demonstrates:
 * - Aggregation (Quiz has-many Questions)
 * - Domain validation and exception throwing (EmptyQuizException, InvalidQuestionException)
 */
public class Quiz {

    private final String quizId;
    private String title;
    private String description;
    private String topic;
    private DifficultyLevel difficulty;
    private String targetAgeGroup;
    private final List<Question> questions;

    public Quiz(String quizId, String title, String description, String topic, DifficultyLevel difficulty, String targetAgeGroup) {
        if (quizId == null || quizId.trim().isEmpty()) {
            throw new IllegalArgumentException("Quiz ID cannot be null or empty!");
        }
        if (title == null || title.trim().isEmpty()) {
            throw new IllegalArgumentException("Quiz title cannot be null or empty!");
        }
        this.quizId = quizId.trim().toUpperCase();
        this.title = title.trim();
        this.description = (description != null) ? description.trim() : "";
        this.topic = (topic != null) ? topic.trim() : "General Java";
        this.difficulty = (difficulty != null) ? difficulty : DifficultyLevel.MEDIUM;
        this.targetAgeGroup = (targetAgeGroup != null && !targetAgeGroup.trim().isEmpty()) ? targetAgeGroup.trim() : "College (18-22)";
        this.questions = new ArrayList<>();
    }

    public Quiz(String quizId, String title, String description, String topic, DifficultyLevel difficulty) {
        this(quizId, title, description, topic, difficulty, "College (18-22)");
    }

    public String getTargetAgeGroup() {
        return targetAgeGroup;
    }

    public void setTargetAgeGroup(String targetAgeGroup) {
        if (targetAgeGroup != null && !targetAgeGroup.trim().isEmpty()) {
            this.targetAgeGroup = targetAgeGroup.trim();
        }
    }

    public String getQuizId() {
        return quizId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        if (title != null && !title.trim().isEmpty()) {
            this.title = title.trim();
        }
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public DifficultyLevel getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(DifficultyLevel difficulty) {
        this.difficulty = difficulty;
    }

    public List<Question> getQuestions() {
        return Collections.unmodifiableList(questions);
    }

    public int getQuestionCount() {
        return questions.size();
    }

    /**
     * Adds a polymorphic Question to the quiz.
     * Throws InvalidQuestionException if null or duplicate ID.
     */
    public void addQuestion(Question question) throws InvalidQuestionException {
        if (question == null) {
            throw new InvalidQuestionException("Cannot add a null question to the quiz!");
        }
        for (Question q : questions) {
            if (q.getId() == question.getId()) {
                throw new InvalidQuestionException("Question with ID " + question.getId() + " already exists in this quiz!");
            }
        }
        questions.add(question);
    }

    public boolean removeQuestion(int questionId) {
        return questions.removeIf(q -> q.getId() == questionId);
    }

    public int getTotalMarks() {
        int total = 0;
        for (Question q : questions) {
            total += q.getMarks();
        }
        return total;
    }

    /**
     * Verifies that the quiz is ready to be conducted.
     * Throws EmptyQuizException if no questions are present.
     */
    public void validateForConduct() throws EmptyQuizException {
        if (questions.isEmpty()) {
            throw new EmptyQuizException(quizId);
        }
    }

    @Override
    public String toString() {
        return String.format("[%s] %s | Age: %s | Topic: %s | Level: %s | Questions: %d | Total Marks: %d",
                quizId, title, targetAgeGroup, topic, difficulty.getDisplayName(), questions.size(), getTotalMarks());
    }
}
