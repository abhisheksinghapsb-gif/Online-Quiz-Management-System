package com.ait.quiz.util;

import java.util.Scanner;

/**
 * Utility helper for robust console input handling and validation.
 * Demonstrates:
 * - Method Overloading (compile-time polymorphism)
 * - Defensive programming and Exception Handling against input mismatches
 */
public class InputValidator {

    /**
     * Reads a validated integer within a specified range [min, max].
     */
    public static int readInteger(Scanner scanner, String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            try {
                int value = Integer.parseInt(input);
                if (value < min || value > max) {
                    System.out.printf("   [!] Error: Value must be between %d and %d. Please try again.%n", min, max);
                    continue;
                }
                return value;
            } catch (NumberFormatException nfe) {
                System.out.println("   [!] Error: Invalid numeric input! Please enter a valid whole number.");
            }
        }
    }

    /**
     * Overloaded method: Reads any valid integer without range constraints.
     * Demonstrates Method Overloading.
     */
    public static int readInteger(Scanner scanner, String prompt) {
        return readInteger(scanner, prompt, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    /**
     * Reads a valid floating-point number.
     */
    public static double readDouble(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            try {
                return Double.parseDouble(input);
            } catch (NumberFormatException nfe) {
                System.out.println("   [!] Error: Invalid number! Please enter a valid decimal number (e.g. 5 or 2.5).");
            }
        }
    }

    /**
     * Reads a non-empty string prompt from console.
     */
    public static String readString(Scanner scanner, String prompt, boolean allowEmpty) {
        while (true) {
            System.out.print(prompt);
            String line = scanner.nextLine().trim();
            if (!allowEmpty && line.isEmpty()) {
                System.out.println("   [!] Error: Input cannot be blank! Please provide a value.");
                continue;
            }
            return line;
        }
    }

    /**
     * Overloaded method: Reads non-empty string by default.
     * Demonstrates Method Overloading.
     */
    public static String readString(Scanner scanner, String prompt) {
        return readString(scanner, prompt, false);
    }

    /**
     * Prompts for confirmation (Y/N).
     */
    public static boolean readYesNo(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt + " (Y/N): ");
            String ans = scanner.nextLine().trim().toUpperCase();
            if (ans.equals("Y") || ans.equals("YES")) {
                return true;
            } else if (ans.equals("N") || ans.equals("NO")) {
                return false;
            }
            System.out.println("   [!] Please enter 'Y' for Yes or 'N' for No.");
        }
    }
}
