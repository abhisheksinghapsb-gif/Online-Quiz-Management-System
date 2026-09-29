package com.ait.quiz.service;

import com.ait.quiz.exception.DuplicateQuizException;
import com.ait.quiz.exception.InvalidQuestionException;
import com.ait.quiz.exception.QuizNotFoundException;
import com.ait.quiz.model.DifficultyLevel;
import com.ait.quiz.model.Question;
import com.ait.quiz.model.Quiz;
import com.ait.quiz.model.QuizAttempt;

import java.util.List;

/**
 * Core interface defining lifecycle operations on quizzes and attempts.
 * Demonstrates Unit III concept: Interfaces (defining contract for Quiz operations).
 */
public interface QuizOperations {

    /**
     * Creates a new quiz in the repository.
     * Throws DuplicateQuizException if the quizId is already taken.
     */
    void createQuiz(Quiz quiz) throws DuplicateQuizException;

    /**
     * Adds a polymorphic Question to the designated Quiz.
     * Throws QuizNotFoundException if target quiz doesn't exist,
     * or InvalidQuestionException if the question violates integrity rules.
     */
    void addQuestionToQuiz(String quizId, Question question) 
            throws QuizNotFoundException, InvalidQuestionException;

    /**
     * Retrieves a quiz by its unique ID.
     * Throws QuizNotFoundException if not found.
     */
    Quiz getQuiz(String quizId) throws QuizNotFoundException;

    /**
     * Returns all quizzes registered in the system.
     */
    List<Quiz> getAllQuizzes();

    /**
     * Overloaded search method: Finds quizzes matching a topic keyword.
     */
    List<Quiz> searchQuiz(String topic);

    /**
     * Overloaded search method: Finds quizzes matching both topic and difficulty level.
     */
    List<Quiz> searchQuiz(String topic, DifficultyLevel level);

    /**
     * Deletes a quiz by its ID.
     * Throws QuizNotFoundException if not found.
     */
    boolean deleteQuiz(String quizId) throws QuizNotFoundException;

    /**
     * Stores a student's completed quiz attempt.
     */
    void recordAttempt(QuizAttempt attempt);

    /**
     * Retrieves all recorded quiz attempts.
     */
    List<QuizAttempt> getAllAttempts();

    /**
     * Retrieves all quiz attempts by a specific student roll number.
     */
    List<QuizAttempt> getAttemptsByStudent(String rollNumber);

    /**
     * Returns total count of registered quizzes.
     */
    int getQuizCount();
}
