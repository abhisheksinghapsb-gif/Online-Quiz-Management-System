package com.ait.quiz.exception;

/**
 * Thrown when a user provides an answer or option that does not conform
 * to the allowed choices (e.g. non-existent option, illegal format).
 */
public class InvalidOptionException extends QuizException {

    private final String chosenOption;
    private final String expectedFormat;

    public InvalidOptionException(String chosenOption, String expectedFormat) {
        super("Invalid option selected: '" + chosenOption + "'. Expected format/range: [" + expectedFormat + "]");
        this.chosenOption = chosenOption;
        this.expectedFormat = expectedFormat;
    }

    public String getChosenOption() {
        return chosenOption;
    }

    public String getExpectedFormat() {
        return expectedFormat;
    }
}
