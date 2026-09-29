package com.ait.quiz.util;

/**
 * Helper class for rendering formatted console output, banners, and menus.
 */
public class ConsoleUI {

    public static final String SEPARATOR_DOUBLE = "================================================================================";
    public static final String SEPARATOR_SINGLE = "--------------------------------------------------------------------------------";

    public static void printHeader(String title) {
        System.out.println(SEPARATOR_DOUBLE);
        int totalWidth = 80;
        int padding = Math.max(0, (totalWidth - title.length()) / 2);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < padding; i++) sb.append(" ");
        sb.append(title);
        System.out.println(sb.toString());
        System.out.println(SEPARATOR_DOUBLE);
    }

    public static void printSubHeader(String title) {
        System.out.println(SEPARATOR_SINGLE);
        System.out.println(" >> " + title);
        System.out.println(SEPARATOR_SINGLE);
    }

    public static void printSuccess(String message) {
        System.out.println(" [SUCCESS] " + message);
    }

    public static void printError(String message) {
        System.out.println(" [ERROR] " + message);
    }

    public static void printWarning(String message) {
        System.out.println(" [WARNING] " + message);
    }

    public static void printInfo(String message) {
        System.out.println(" [INFO] " + message);
    }
}
