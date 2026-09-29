import os
import zipfile
from datetime import datetime

base_dir = r"g:\aunty gravity projects\java project"
src_dir = os.path.join(base_dir, "src")

# Logical grouping of the 25 files
file_order = [
    # 1. Custom Exception Hierarchy (Unit IV)
    ("UNIT IV: EXCEPTION HANDLING HIERARCHY", [
        "src/com/ait/quiz/exception/QuizException.java",
        "src/com/ait/quiz/exception/QuizNotFoundException.java",
        "src/com/ait/quiz/exception/DuplicateQuizException.java",
        "src/com/ait/quiz/exception/InvalidOptionException.java",
        "src/com/ait/quiz/exception/InvalidQuestionException.java",
        "src/com/ait/quiz/exception/EmptyQuizException.java"
    ]),
    # 2. Domain Models & Abstract Classes (Unit III)
    ("UNIT III: ABSTRACT CLASSES & QUESTION MODELS", [
        "src/com/ait/quiz/model/DifficultyLevel.java",
        "src/com/ait/quiz/model/Question.java",
        "src/com/ait/quiz/model/MultipleChoiceQuestion.java",
        "src/com/ait/quiz/model/TrueFalseQuestion.java",
        "src/com/ait/quiz/model/NumericQuestion.java",
        "src/com/ait/quiz/model/User.java",
        "src/com/ait/quiz/model/Student.java",
        "src/com/ait/quiz/model/Instructor.java",
        "src/com/ait/quiz/model/Quiz.java",
        "src/com/ait/quiz/model/QuizAttempt.java"
    ]),
    # 3. Interfaces & Strategy Polymorphism (Unit III)
    ("UNIT III: INTERFACES & STRATEGY PATTERN GRADING POLICIES", [
        "src/com/ait/quiz/service/QuizOperations.java",
        "src/com/ait/quiz/service/QuizEvaluator.java",
        "src/com/ait/quiz/service/StandardGradingPolicy.java",
        "src/com/ait/quiz/service/NegativeMarkingGradingPolicy.java",
        "src/com/ait/quiz/service/QuizManager.java"
    ]),
    # 4. Utilities & Defensive Validation
    ("UNIT III & IV: DEFENSIVE UTILITIES & CONSOLE FORMATTING", [
        "src/com/ait/quiz/util/InputValidator.java",
        "src/com/ait/quiz/util/ConsoleUI.java"
    ]),
    # 5. Application Entry Point & Automated Test Harness
    ("APPLICATION ENTRY POINT & CIE-2 VIVA DEMONSTRATION HARNESS", [
        "src/com/ait/quiz/main/QuizApplication.java"
    ]),
    # 6. Embedded Java HTTP Web Server
    ("EMBEDDED LIGHTWEIGHT JAVA HTTP REST WEB SERVER", [
        "src/com/ait/quiz/web/QuizWebServer.java"
    ])
]

# Generate Markdown Document
md_lines = []
md_lines.append("# Online Quiz Management System — Complete Java Source Code Compilation")
md_lines.append("")
md_lines.append("> **Institution:** Army Institute of Technology (AIT), Pune  ")
md_lines.append("> **Department:** Department of Information Technology  ")
md_lines.append("> **Course:** Skill Development Laboratory using Java (`BIT25434A0X`)  ")
md_lines.append("> **Evaluation:** Continuous Internal Evaluation 2 (CIE-2) | **Class:** SE IT B  ")
md_lines.append("> **Examiner / Course In-charge:** Mrs. Trupti Najan  ")
md_lines.append("> **Project Group Members:**  ")
md_lines.append("> • **Aditya Yadav** (Roll No: 8108 — Group Leader)  ")
md_lines.append("> • **Abhishekh Singh** (Roll No: 8104)  ")
md_lines.append("> • **Priyam Raj** (Roll No: 8134)  ")
md_lines.append("> • **Utkarsh Chauhan** (Roll No: 8154)  ")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📑 Table of Contents")
md_lines.append("")

doc_file_num = 1
for group_title, files in file_order:
    md_lines.append(f"### {group_title}")
    for rel_path in files:
        fname = os.path.basename(rel_path)
        anchor = fname.lower().replace(".", "")
        md_lines.append(f"{doc_file_num}. [{fname}](#{anchor}) (`{rel_path}`)")
        doc_file_num += 1
    md_lines.append("")

md_lines.append("---")
md_lines.append("")

# Append each file's source code
for group_title, files in file_order:
    md_lines.append(f"## {group_title}")
    md_lines.append("")
    for rel_path in files:
        full_path = os.path.join(base_dir, rel_path.replace("/", os.sep))
        fname = os.path.basename(rel_path)
        with open(full_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        md_lines.append(f"### `{fname}`")
        md_lines.append(f"**Path:** `{rel_path}`  ")
        md_lines.append(f"**Lines of Code:** {len(code.splitlines())}  ")
        md_lines.append("")
        md_lines.append("```java")
        md_lines.append(code)
        md_lines.append("```")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

md_content = "\n".join(md_lines)
md_out_path = os.path.join(base_dir, "docs", "COMPLETE_JAVA_SOURCE_CODE.md")
with open(md_out_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Generated Markdown source file at: {md_out_path} ({len(md_content)} bytes)")

# Generate Plain Text Document (Formatted for Printing / Plain submission)
txt_lines = []
banner = "=" * 80
sub_banner = "-" * 80

txt_lines.append(banner)
txt_lines.append("      ONLINE QUIZ MANAGEMENT SYSTEM - COMPLETE JAVA SOURCE CODE")
txt_lines.append("               ARMY INSTITUTE OF TECHNOLOGY (AIT), PUNE")
txt_lines.append("              DEPARTMENT OF INFORMATION TECHNOLOGY (SE IT B)")
txt_lines.append("    Course: Skill Development Laboratory using Java (BIT25434A0X) - CIE-2")
txt_lines.append("                 Course In-charge: Mrs. Trupti Najan")
txt_lines.append(banner)
txt_lines.append("PROJECT GROUP MEMBERS:")
txt_lines.append("  1. Aditya Yadav     (Roll No: 8108 - Group Leader)")
txt_lines.append("  2. Abhishekh Singh  (Roll No: 8104)")
txt_lines.append("  3. Priyam Raj       (Roll No: 8134)")
txt_lines.append("  4. Utkarsh Chauhan  (Roll No: 8154)")
txt_lines.append("")
txt_lines.append("MANDATORY SYLLABUS CONCEPTS DEMONSTRATED:")
txt_lines.append("  [Unit III] Abstract Classes: Base Question & User hierarchy.")
txt_lines.append("  [Unit III] Interfaces: QuizOperations & QuizEvaluator (Strategy Pattern).")
txt_lines.append("  [Unit III] Polymorphism: Dynamic Method Dispatch & Overloaded Search.")
txt_lines.append("  [Unit IV]  Exception Handling: 5-Tier Custom Checked Hierarchy & Zero-Crash.")
txt_lines.append(banner)
txt_lines.append("")

f_idx = 1
for group_title, files in file_order:
    txt_lines.append("")
    txt_lines.append(banner)
    txt_lines.append(f" SECTION: {group_title}")
    txt_lines.append(banner)
    for rel_path in files:
        full_path = os.path.join(base_dir, rel_path.replace("/", os.sep))
        fname = os.path.basename(rel_path)
        with open(full_path, "r", encoding="utf-8") as f:
            code = f.read()
        
        txt_lines.append("")
        txt_lines.append(sub_banner)
        txt_lines.append(f" File #{f_idx}: {fname}  [Path: {rel_path}]")
        txt_lines.append(sub_banner)
        txt_lines.append("")
        
        # Add line numbers for academic clarity
        for line_num, line in enumerate(code.splitlines(), start=1):
            txt_lines.append(f"{line_num:4d} | {line}")
        
        txt_lines.append("")
        f_idx += 1

txt_content = "\n".join(txt_lines)
txt_out_path = os.path.join(base_dir, "Online_Quiz_Management_System_Complete_Source_Code.txt")
with open(txt_out_path, "w", encoding="utf-8") as f:
    f.write(txt_content)

print(f"Generated Plain Text source file at: {txt_out_path} ({len(txt_content)} bytes)")

# Generate ZIP archive containing entire src/, scripts, docs
zip_out_path = os.path.join(base_dir, "Online_Quiz_Management_System_Java_Source_Code.zip")
with zipfile.ZipFile(zip_out_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            full = os.path.join(root, file)
            rel = os.path.relpath(full, base_dir)
            zipf.write(full, rel)
    
    # Add batch files
    for b in ["compile.bat", "run.bat", "run_web.bat", "run_tests.bat"]:
        full_b = os.path.join(base_dir, b)
        if os.path.exists(full_b):
            zipf.write(full_b, b)
            
    # Add txt file
    zipf.write(txt_out_path, "Online_Quiz_Management_System_Complete_Source_Code.txt")

print(f"Generated ZIP bundle at: {zip_out_path} ({os.path.getsize(zip_out_path)} bytes)")
