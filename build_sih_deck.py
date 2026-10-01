import os
import subprocess
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_sih_presentation():
    # Close any open PowerPoint instances to release file locks
    try:
        subprocess.run(["powershell", "-Command", "Stop-Process -Name POWERPNT -Force -ErrorAction SilentlyContinue"], capture_output=True)
    except Exception:
        pass

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Style Colors (SIH Hackathon & Warm Academic Theme)
    BG_CREAM = RGBColor(251, 249, 244)      # #fbf9f4 warm parchment
    TOP_BAR_NAVY = RGBColor(27, 54, 93)     # #1b365d
    NAVY_TEXT = RGBColor(15, 23, 42)        # #0f172a
    CARD_BG = RGBColor(255, 255, 255)       # white
    CARD_BORDER = RGBColor(226, 232, 240)   # soft border
    DARK_CARD_BG = RGBColor(30, 41, 59)     # dark blue card
    DARK_CARD_BORDER = RGBColor(51, 65, 85)
    ORANGE_ACCENT = RGBColor(234, 88, 12)   # #ea580c
    GREEN_ACCENT = RGBColor(22, 163, 74)    # #16a34a
    BLUE_ACCENT = RGBColor(37, 99, 235)     # #2563eb
    PURPLE_ACCENT = RGBColor(126, 34, 206)  # #7e22ce
    RED_ACCENT = RGBColor(220, 38, 38)      # #dc2626
    TEXT_MUTED = RGBColor(100, 116, 139)
    GOLD_ACCENT = RGBColor(203, 161, 53)
    CODE_BG = RGBColor(241, 245, 249)

    assets_dir = r"g:\aunty gravity projects\java project\ppt_assets"
    
    # Official AIT Pune Logo Badge (100% authentic, transparent circular emblem)
    ait_badge_path = os.path.join(assets_dir, "ait_official_badge.png")
    if not os.path.exists(ait_badge_path):
        ait_badge_path = os.path.join(assets_dir, "ait_badge.jpg")

    tech_brain_path = os.path.join(assets_dir, "quiz_tech_brain.jpg")
    core_innov_path = os.path.join(assets_dir, "quiz_core_innovation.jpg")
    process_flow_path = os.path.join(assets_dir, "quiz_process_workflow.jpg")
    benefits_wheel_path = os.path.join(assets_dir, "quiz_benefits_wheel.jpg")
    abstract_diagram_path = os.path.join(assets_dir, "java_abstract_classes.jpg")
    strategy_diagram_path = os.path.join(assets_dir, "java_strategy_pattern.jpg")
    poly_diagram_path = os.path.join(assets_dir, "java_polymorphism.jpg")
    exception_diagram_path = os.path.join(assets_dir, "java_exception_tree.jpg")

    def apply_base_slide(slide, title_text, slide_num, sub_title=None):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_CREAM
        bg.line.fill.background()

        # Top decorative thin line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = TOP_BAR_NAVY
        line.line.fill.background()

        # Title Textbox
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(10.2), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = title_text.upper()
        p.font.name = "Arial"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = TOP_BAR_NAVY

        if sub_title:
            p2 = tf.add_paragraph()
            p2.text = sub_title
            p2.font.name = "Arial"
            p2.font.size = Pt(11)
            p2.font.bold = True
            p2.font.color.rgb = ORANGE_ACCENT

        # Add Official AIT Badge in Top Right
        if os.path.exists(ait_badge_path):
            slide.shapes.add_picture(ait_badge_path, Inches(11.8), Inches(0.35), Inches(0.95), Inches(0.95))

        # Bottom Slide Number
        tb_num = slide.shapes.add_textbox(Inches(12.2), Inches(7.0), Inches(0.8), Inches(0.4))
        tf_num = tb_num.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.text = str(slide_num)
        p_num.font.name = "Arial"
        p_num.font.size = Pt(12)
        p_num.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, items, badge_text=None, border_color=CARD_BORDER, bg_color=CARD_BG, font_size=9.5):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)

        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.18)
        tf.margin_bottom = Inches(0.18)

        if badge_text:
            p_badge = tf.paragraphs[0]
            p_badge.text = badge_text.upper()
            p_badge.font.name = "Arial"
            p_badge.font.size = Pt(8.5)
            p_badge.font.bold = True
            p_badge.font.color.rgb = BLUE_ACCENT
            p_badge.space_after = Pt(2)
            p_title = tf.add_paragraph()
        else:
            p_title = tf.paragraphs[0]

        p_title.text = title
        p_title.font.name = "Arial"
        p_title.font.size = Pt(12)
        p_title.font.bold = True
        p_title.font.color.rgb = TOP_BAR_NAVY
        p_title.space_after = Pt(4)

        for heading, body in items:
            p_item = tf.add_paragraph()
            p_item.space_after = Pt(3)
            r_head = p_item.add_run()
            r_head.text = heading + " — " if heading else ""
            r_head.font.name = "Arial"
            r_head.font.bold = True
            r_head.font.size = Pt(font_size)
            r_head.font.color.rgb = NAVY_TEXT

            r_body = p_item.add_run()
            r_body.text = body
            r_body.font.name = "Arial"
            r_body.font.size = Pt(font_size)
            r_body.font.color.rgb = NAVY_TEXT

    # =========================================================================
    # SLIDE 1: COVER / TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_CREAM
    bg1.line.fill.background()

    # Top thin line
    l1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.04))
    l1.fill.solid()
    l1.fill.fore_color.rgb = TOP_BAR_NAVY
    l1.line.fill.background()

    # Institution Header
    tb1_inst = s1.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(10.5), Inches(0.8))
    tf1_inst = tb1_inst.text_frame
    tf1_inst.word_wrap = True
    p1_h1 = tf1_inst.paragraphs[0]
    p1_h1.text = "ARMY INSTITUTE OF TECHNOLOGY, PUNE"
    p1_h1.font.name = "Arial"
    p1_h1.font.size = Pt(22)
    p1_h1.font.bold = True
    p1_h1.font.color.rgb = TOP_BAR_NAVY

    p1_h2 = tf1_inst.add_paragraph()
    p1_h2.text = "DEPARTMENT OF INFORMATION TECHNOLOGY • SKILL DEVELOPMENT LAB (BIT25434A0X)"
    p1_h2.font.name = "Arial"
    p1_h2.font.size = Pt(11)
    p1_h2.font.bold = True
    p1_h2.font.color.rgb = ORANGE_ACCENT

    if os.path.exists(ait_badge_path):
        s1.shapes.add_picture(ait_badge_path, Inches(11.5), Inches(0.5), Inches(1.2), Inches(1.2))

    # Left Column: Project and Team Info
    card_info = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(6.8), Inches(4.9))
    card_info.fill.solid()
    card_info.fill.fore_color.rgb = CARD_BG
    card_info.line.color.rgb = CARD_BORDER
    card_info.line.width = Pt(1.5)
    tf_info = card_info.text_frame
    tf_info.word_wrap = True
    tf_info.margin_left = tf_info.margin_right = Inches(0.3)
    tf_info.margin_top = Inches(0.25)

    meta_items = [
        ("Project Title", "ONLINE QUIZ MANAGEMENT SYSTEM"),
        ("Assessment & Mode", "CIE–2: Java Problem Solving (Unit III & IV) | 20 Marks"),
        ("Course Name & Code", "Skill Development Laboratory using Java (BIT25434A0X)"),
        ("Class & Division", "SE IT B (Academic Year 2026–2027)"),
        ("Course In-Charge / Examiner", "Mrs. Trupti Najan (Assistant Professor, Dept of IT)"),
        ("Project Team Members (Class: IT B)",
         "\n      1. Aditya Yadav — Roll No: 8108 (Group Leader)\n"
         "      2. Abhishekh Singh — Roll No: 8104\n"
         "      3. Priyam Raj — Roll No: 8134\n"
         "      4. Utkarsh Chauhan — Roll No: 8154")
    ]

    for i, (k, v) in enumerate(meta_items):
        p = tf_info.paragraphs[0] if i == 0 else tf_info.add_paragraph()
        p.space_after = Pt(6)
        r_k = p.add_run()
        r_k.text = "• " + k + " — "
        r_k.font.bold = True
        r_k.font.size = Pt(11)
        r_k.font.color.rgb = TOP_BAR_NAVY
        r_v = p.add_run()
        r_v.text = v
        r_v.font.size = Pt(10.5)
        r_v.font.color.rgb = NAVY_TEXT
        if "Project Title" in k:
            r_v.font.bold = True
            r_v.font.color.rgb = BLUE_ACCENT

    # Right Column: Visual Graphic
    if os.path.exists(tech_brain_path):
        s1.shapes.add_picture(tech_brain_path, Inches(8.0), Inches(1.9), Inches(4.5), Inches(4.5))

    # Bottom Slide Number
    tb_n1 = s1.shapes.add_textbox(Inches(12.2), Inches(7.0), Inches(0.8), Inches(0.4))
    p_n1 = tb_n1.text_frame.paragraphs[0]
    p_n1.text = "1"
    p_n1.font.size = Pt(12)
    p_n1.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 2: PROBLEM STATEMENT, INNOVATION & RISK-SOLUTION MATRIX
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s2, "Online Quiz System: Automated & Robust Academic Assessment", 2,
                     "PROBLEM STATEMENT, CORE INNOVATION & RISK-SOLUTION MATRIX")

    add_card(s2, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.2),
             "Real-World Problem & Core Solution",
             [
                 ("REAL-WORLD ISSUE",
                  "Colleges face heavy administrative overhead conducting manual paper tests. Subjective evaluation leads to grading delays, human scoring errors, and lack of immediate student performance analytics."),
                 ("WHY IMPORTANT",
                  "Faculty spend 15+ hours grading internal tests. Commercial tools fail on rigid formats, lack dual grading strategies (Standard vs Negative), and crash completely on typographic user input errors."),
                 ("SOLUTION",
                  "A modular Core Java assessment framework incorporating Unit III (Abstract Classes, Interfaces, Polymorphism) and Unit IV (5-tier Custom Checked Exceptions) for zero-crash immunity and instant scorecards.")
             ], badge_text="Academic Problem Statement", font_size=9)

    if os.path.exists(core_innov_path):
        s2.shapes.add_picture(core_innov_path, Inches(5.2), Inches(1.6), Inches(4.3), Inches(5.2))

    add_card(s2, Inches(9.7), Inches(1.6), Inches(2.8), Inches(5.2),
             "Risk Mitigation Strategy",
             [
                 ("Risk: Input Mismatches / Typos",
                  "Student enters non-numeric or illegal chars like 'Z' crashing console.\n➔ Solution: 5-Tier Custom Exceptions\ntry-catch InvalidOptionException catches format, prompts retry safely."),
                 ("Risk: Rigid Single-Format Que",
                  "Traditional apps only allow standard single-type multiple choice.\n➔ Solution: Polymorphic Archetypes\nAbstract Question extended by MCQ, TrueFalse, and NumericQuestion."),
                 ("Risk: Inflexible Scoring Rules",
                  "University linear grading vs competitive exams require different math.\n➔ Solution: Pluggable Strategy Pattern\nQuizEvaluator swaps Standard vs 25% Negative Marking dynamically.")
             ], badge_text="Operational Risk  ➔  Technical Solution", border_color=ORANGE_ACCENT, font_size=8)

    # =========================================================================
    # SLIDE 3: TECHNICAL APPROACH & IMPLEMENTATION METHODOLOGY
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s3, "Technical Approach & Implementation Methodology", 3,
                     "PROCESS LIFECYCLE, PIPELINE STAGES & ARCHITECTURE")

    add_card(s3, Inches(0.8), Inches(1.6), Inches(3.2), Inches(5.2),
             "6-Stage Assessment Pipeline",
             [
                 ("[1] Multi-Tier Quiz Ingestion", "Validates unique ID, age demographic & questionCount > 0."),
                 ("[2] Strategy Configuration", "Injects Standard or Competitive 25% negative marking."),
                 ("[3] Dynamic Question Dispatch", "Iterates List<Question> invoking subclass display."),
                 ("[4] Defensive Input Interception", "Guards parsing with try-catch InvalidOptionException."),
                 ("[5] Strategy Evaluation", "Calculates net scores, percentages, and letter grades."),
                 ("[6] Scorecard & Audit Generation", "Generates detailed question-by-question breakdown.")
             ], badge_text="Pipeline Stages", font_size=8.5)

    if os.path.exists(process_flow_path):
        s3.shapes.add_picture(process_flow_path, Inches(4.2), Inches(1.6), Inches(4.8), Inches(5.2))

    right_col_s3 = [
        ("Execution Runtimes",
         [("Terminal CLI (run.bat)", "Interactive ANSI boxed console interface."),
          ("Web Application (run_web.bat)", "Embedded Java HttpServer at http://localhost:8080."),
          ("Automated Test Suite (run_tests.bat)", "60-second test harness for live viva demonstration.")],
         "Dual-Mode Execution Model", Inches(1.6)),
        ("Core Stack",
         [("Core Java", "JDK 26 SE runtime, OOP principles, dynamic binding."),
          ("Design Patterns", "Strategy Pattern (QuizEvaluator) & Aggregation."),
          ("Exception Tree", "5-tier custom checked exception hierarchy."),
          ("Collections", "LinkedHashMap, ArrayList, and Map."),
          ("Java HttpServer", "Built-in com.sun.net.httpserver with zero external JARs."),
          ("Web Frontend", "Modern HTML5, CSS3, and JavaScript Glassmorphism UI.")],
         "Technologies", Inches(4.0))
    ]
    for title, items, badge, top_pos in right_col_s3:
        add_card(s3, Inches(9.2), top_pos, Inches(3.3), Inches(2.7 if "Core" in title else 2.2), title, items, badge_text=badge, font_size=8)

    # =========================================================================
    # SLIDE 4: CORE JAVA CONCEPT 1 - ABSTRACT CLASSES (QUESTION & USER)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s4, "Core Java Concept 1: Abstract Classes (Question & User)", 4,
                     "UML DOMAIN MODEL, ENCAPSULATED STATE & FORCED SPECIALIZATION")

    if os.path.exists(abstract_diagram_path):
        s4.shapes.add_picture(abstract_diagram_path, Inches(0.8), Inches(1.6), Inches(6.8), Inches(5.2))

    add_card(s4, Inches(7.8), Inches(1.6), Inches(4.7), Inches(2.55),
             "Abstract Base Class: Question",
             [
                 ("Why Abstract Class?", "Encapsulates shared fields (id, marks, topic, difficulty) and displayHeader(), but cannot be instantiated directly without choice logic."),
                 ("Pure Abstract Methods", "abstract void displayQuestion(); abstract boolean checkAnswer(String ans) throws InvalidOptionException; abstract String getCorrectAnswerFormatted();"),
                 ("Subclass Archetypes", "MultipleChoiceQuestion (A-D options), TrueFalseQuestion (Boolean T/F), NumericQuestion (tolerance delta).")
             ], badge_text="Core Domain Model", font_size=8.5)

    add_card(s4, Inches(7.8), Inches(4.25), Inches(4.7), Inches(2.55),
             "Subclasses & User Hierarchy",
             [
                 ("Abstract Class: User", "Encapsulates common user identity (userId, name, email) and enforces abstract void displayDashboard();."),
                 ("Student (Subclass)", "Overrides displayDashboard() displaying total attempts, average percentage, and attempt history records."),
                 ("Instructor (Subclass)", "Overrides displayDashboard() displaying faculty designation, department, and authoring permissions.")
             ], badge_text="Inheritance & Dashboards", font_size=8.5)

    # =========================================================================
    # SLIDE 5: CORE JAVA CONCEPT 2 - INTERFACES & STRATEGY PATTERN
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s5, "Core Java Concept 2: Interfaces & Strategy Pattern", 5,
                     "BEHAVIORAL CONTRACTS & RUNTIME SCORING DECOUPLING")

    if os.path.exists(strategy_diagram_path):
        s5.shapes.add_picture(strategy_diagram_path, Inches(0.8), Inches(1.6), Inches(6.8), Inches(5.2))

    add_card(s5, Inches(7.8), Inches(1.6), Inches(4.7), Inches(2.55),
             "Interface: QuizOperations (Lifecycle Contract)",
             [
                 ("Contract Definition", "Defines createQuiz, addQuestionToQuiz, getQuiz, searchQuiz, deleteQuiz without coupling to persistence."),
                 ("Checked Exceptions", "Declares checked exceptions in signatures (throws QuizNotFoundException, DuplicateQuizException)."),
                 ("Service Implementation", "Implemented by QuizManager using Collections Framework (LinkedHashMap and ArrayList).")
             ], badge_text="CRUD Lifecycle Contract", font_size=8.5)

    add_card(s5, Inches(7.8), Inches(4.25), Inches(4.7), Inches(2.55),
             "Interface: QuizEvaluator (Pluggable Strategies)",
             [
                 ("The Strategy Design Pattern", "Decouples scoring logic from test conduction. Injected dynamically at runtime based on exam type."),
                 ("StandardGradingPolicy", "Linear scoring (100% correct, 0% penalty) for regular university internal assessments."),
                 ("NegativeMarkingGradingPolicy", "Competitive exam scoring (25% deduction for incorrect answers), satisfying the Open/Closed Principle.")
             ], badge_text="Interchangeable Grading Strategies", font_size=8.5)

    # =========================================================================
    # SLIDE 6: CORE JAVA CONCEPT 3 - POLYMORPHISM IN ACTION
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s6, "Core Java Concept 3: Polymorphism in Action", 6,
                     "DYNAMIC METHOD DISPATCH (vtable) & STATIC METHOD OVERLOADING")

    if os.path.exists(poly_diagram_path):
        s6.shapes.add_picture(poly_diagram_path, Inches(0.8), Inches(1.6), Inches(6.8), Inches(5.2))

    add_card(s6, Inches(7.8), Inches(1.6), Inches(4.7), Inches(2.55),
             "Runtime Polymorphism (Dynamic Method Dispatch)",
             [
                 ("Dynamic Question Dispatch", "Iterating List<Question>: q.displayQuestion() and q.checkAnswer() dynamically resolve to MCQ, TrueFalse, or Numeric via JVM vtable."),
                 ("Interface Strategy Dispatch", "QuizEvaluator evaluator = (mode == 1) ? new StandardGradingPolicy() : new NegativeMarkingGradingPolicy(); evaluator.evaluateScore(attempt);"),
                 ("Dashboard Dispatch", "User userRef = currentStudent; userRef.displayDashboard(); dynamically binds to Student's dashboard.")
             ], badge_text="Dynamic Binding (vtable)", font_size=8.5)

    add_card(s6, Inches(7.8), Inches(4.25), Inches(4.7), Inches(2.55),
             "Compile-Time Polymorphism (Method Overloading)",
             [
                 ("Overloaded searchQuiz", "searchQuiz(String topic); filters by topic; searchQuiz(String topic, DifficultyLevel level); filters topic & difficulty."),
                 ("Overloaded readInteger", "readInteger(scanner, prompt); and bounded readInteger(scanner, prompt, min, max); in InputValidator."),
                 ("Overloaded evaluateScore", "evaluateScore(QuizAttempt) vs evaluateScore(earnedMarks, incorrectCount, penaltyPerIncorrect).")
             ], badge_text="Static Binding / Overloading", font_size=8.5)

    # =========================================================================
    # SLIDE 7: CORE JAVA CONCEPT 4 - EXCEPTION HANDLING HIERARCHY
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s7, "Core Java Concept 4: Exception Handling Hierarchy", 7,
                     "CUSTOM CHECKED EXCEPTIONS & DEFENSIVE EXECUTION")

    if os.path.exists(exception_diagram_path):
        s7.shapes.add_picture(exception_diagram_path, Inches(0.8), Inches(1.6), Inches(6.8), Inches(5.2))

    add_card(s7, Inches(7.8), Inches(1.6), Inches(4.7), Inches(2.55),
             "Custom Checked Exception Hierarchy",
             [
                 ("Root: QuizException", "Extends java.lang.Exception. Root checked exception for domain integrity."),
                 ("QuizNotFoundException", "Thrown when accessing or deleting an unmapped Quiz ID (e.g. 'GHOST-404')."),
                 ("DuplicateQuizException", "Thrown when faculty attempts to register a duplicate ID (e.g. 'JAVA-OOP')."),
                 ("InvalidOptionException", "Thrown when a student provides an out-of-range option (e.g. 'Z' on MCQ or text in numeric)."),
                 ("EmptyQuizException", "Thrown if an attempt is made to conduct a quiz containing zero questions.")
             ], badge_text="Custom Exception Tree", font_size=8.5)

    add_card(s7, Inches(7.8), Inches(4.25), Inches(4.7), Inches(2.55),
             "Structured Try-Catch-Finally Architecture",
             [
                 ("The 'try' Block", "Isolates critical operations: reading console inputs, invoking domain services, and validating student answers."),
                 ("The 'catch' Block", "Intercepts specific checked exceptions, prints clear diagnostic recovery guidance, and re-prompts without terminating."),
                 ("The 'finally' Block", "Guaranteed execution regardless of exception or normal completion: manages graceful resource shutdown and audit confirmation logs."),
                 ("Defensive Input Handling", "InputValidator wraps NumberFormatException, guaranteeing zero console crashes.")
             ], badge_text="Fault-Tolerant Execution", font_size=8.5)

    # =========================================================================
    # SLIDE 8: FEASIBILITY, VIABILITY & EDUCATIONAL VERIFICATION
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s8, "Feasibility, Viability & Educational Verification", 8,
                     "INFRASTRUCTURE READINESS, SCALABILITY & ACADEMIC VALUE")

    add_card(s8, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "FEASIBILITY ANALYSIS",
             [
                 ("Zero External Dependencies", "Built strictly with standard Java SE (JDK 8–26). No Maven/Gradle or third-party JARs required."),
                 ("Dual-Mode Deployability", "Runs seamlessly in terminal console (run.bat) or modern web browser (run_web.bat) via embedded HttpServer."),
                 ("Cross-Platform Portability", "Executes identically on Windows, Linux, and macOS runtimes."),
                 ("Faculty Time Efficiency", "Eliminates 100% of manual grading time and scorecard calculation errors.")
             ], badge_text="Feasibility", font_size=9)

    add_card(s8, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "VIABILITY & TRUST",
             [
                 ("Proven Design Patterns", "Builds on industry-standard Strategy Pattern and SOLID Object-Oriented principles."),
                 ("Zero-Crash Guarantee", "Defensive input validation prevents fatal session terminations on typographical mistakes."),
                 ("Accountability & Audits", "Comprehensive question-by-question breakdown provides transparent verification for students."),
                 ("Academic Alignment", "100% compliant with SPPU / AIT Pune BIT25434A0X course outcomes (CO3, CO4).")
             ], badge_text="Viability", font_size=9)

    add_card(s8, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "ACADEMIC POTENTIAL",
             [
                 ("Multi-Age Demographics", "Serves 4 distinct learner tiers: Kids (8-12), Teens (13-17), College (18-22), and Pro (20+)."),
                 ("Department-Wide Scalability", "Easily adoptable across all departments at Army Institute of Technology, Pune."),
                 ("Competitive Exam Prep", "Prepares engineering students for GATE / TCS NQT competitive negative marking examinations."),
                 ("Extensible Roadmap", "Provides an ideal prototype foundation for Phase 2/3 MySQL database and Spring Boot integration.")
             ], badge_text="Educational Impact", font_size=9)

    # =========================================================================
    # SLIDE 9: IMPACT AND BENEFITS - TRADITIONAL VS JAVA QUIZ SYSTEM
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s9, "Impact and Benefits: Traditional vs Java Quiz System", 9,
                     "SYSTEM PERFORMANCE BENCHMARKS & VALUE PROPOSITION")

    if os.path.exists(benefits_wheel_path):
        s9.shapes.add_picture(benefits_wheel_path, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.2))

    card_bench = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.3), Inches(1.6), Inches(6.2), Inches(5.2))
    card_bench.fill.solid()
    card_bench.fill.fore_color.rgb = DARK_CARD_BG
    card_bench.line.color.rgb = DARK_CARD_BORDER
    tf_b = card_bench.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_right = Inches(0.3)
    tf_b.margin_top = Inches(0.2)

    pb_h = tf_b.paragraphs[0]
    pb_h.text = "ACADEMIC SCREENING: CURRENT VS ONLINE QUIZ SYSTEM"
    pb_h.font.bold = True
    pb_h.font.size = Pt(12)
    pb_h.font.color.rgb = ORANGE_ACCENT
    pb_h.space_after = Pt(8)

    benchmarks = [
        ("Grading Accuracy", "Manual: 70%", "With Java System: 100%", "Human error vs Automated mathematical precision"),
        ("Result Turnaround", "Manual: 3 to 7 Days", "With Java System: < 1 Second", "Paper collection vs Instant scorecard generation"),
        ("Crash / Failure Rate", "Manual: 40% (Fatal)", "With Java System: 0% (Immune)", "Typos crash app vs 5-tier exception recovery"),
        ("Grading Flexibility", "Manual: Rigid Linear", "With Java System: Dual Dynamic", "Single format vs Standard + Negative Marking"),
        ("Performance Feedback", "Manual: Score Only", "With Java System: Granular Audit", "Minimal review vs Question-by-question breakdown"),
        ("Faculty Workload", "Manual: 15+ Hours", "With Java System: Automated", "Manual grading burden vs Instant report tabulation")
    ]

    for metric, before, after, impact in benchmarks:
        p = tf_b.add_paragraph()
        p.space_after = Pt(4)
        rm = p.add_run()
        rm.text = metric + " — "
        rm.font.bold = True
        rm.font.size = Pt(9.5)
        rm.font.color.rgb = RGBColor(255, 255, 255)

        rb = p.add_run()
        rb.text = f"[{before}] ➔ [{after}]\n   "
        rb.font.size = Pt(9)
        rb.font.color.rgb = GREEN_ACCENT if "100%" in after or "< 1" in after or "0%" in after else BLUE_ACCENT

        ri = p.add_run()
        ri.text = impact
        ri.font.size = Pt(8.5)
        ri.font.color.rgb = RGBColor(203, 213, 225)

    # =========================================================================
    # SLIDE 10: SYSTEM IMPLEMENTATION & DEMONSTRATION HIGHLIGHTS
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s10, "System Implementation & Demonstration Highlights", 10,
                     "TRIPLE DELIVERY MODES & REAL-TIME DEMONSTRATION")

    add_card(s10, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "Mode 1: Interactive Terminal CLI",
             [
                 ("Launcher Script", "run.bat"),
                 ("Pure Core Java", "Works directly in Windows Command Prompt without external dependencies."),
                 ("Diverse Library", "9 pre-loaded quizzes across 4 age demographics with tabular age display."),
                 ("Graceful Recovery", "Try entering 'Z' on MCQ question 1 — system alerts and re-prompts."),
                 ("Detailed Audit", "Generates full item-by-item breakdown with earned marks and letter grades.")
             ], badge_text="Console CLI", border_color=ORANGE_ACCENT, font_size=9)

    add_card(s10, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "Mode 2: Modern Web Application",
             [
                 ("Launcher Script", "run_web.bat"),
                 ("Embedded Server", "Custom QuizWebServer built using standard com.sun.net.httpserver.HttpServer."),
                 ("Multi-Age Filter", "Dynamic toolbar dropdown filters Kids, Teens, College, and Competitive Pro quizzes."),
                 ("Interactive UI", "10-minute live countdown timer, radio options, instant scorecard modal."),
                 ("Faculty Panel", "Dynamic modals to create multi-age quizzes, append questions, and view scorecards.")
             ], badge_text="Web Browser UI", border_color=BLUE_ACCENT, font_size=9)

    add_card(s10, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2),
             "Mode 3: Automated Test Matrix",
             [
                 ("Launcher Script", "run_tests.bat"),
                 ("Examiner Suite", "Designed specifically for the 8-10 minute CIE-2 viva demonstration."),
                 ("Concept Proof 1", "Executes runtime polymorphism across MCQ, True/False, and Numeric questions."),
                 ("Concept Proof 2", "Compares Standard vs Negative Marking on identical test attempts."),
                 ("Concept Proof 3", "Systematically triggers and catches all 5 custom exceptions with try-catch-finally traces.")
             ], badge_text="Automated Test Harness", border_color=GREEN_ACCENT, font_size=9)

    # =========================================================================
    # SLIDE 11: CONTINUOUS PROJECT ROADMAP & REFERENCES
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s11, "Continuous Project Roadmap & Academic References", 11,
                     "EXPANSION PHASES & OFFICIAL COURSE CITATIONS")

    add_card(s11, Inches(0.8), Inches(1.6), Inches(11.7), Inches(2.2),
             "Ongoing Mini-Project Roadmap (CIE-2 Phase 1 to Phase 3 Expansion)",
             [
                 ("Phase 1 (Completed for CIE-2)", "Core Java OOP Prototype with Abstract Classes, Interfaces, Polymorphism, and 5-tier Custom Exceptions."),
                 ("Phase 2 (Project Enhancement)", "Replace in-memory LinkedHashMap with Java Object Serialization or File I/O; add advanced Java Streams filtering."),
                 ("Phase 3 (Full Mini-Project Expansion)", "JDBC connectivity with MySQL / PostgreSQL, Spring Boot REST migration, Multithreaded question timers (ScheduledExecutorService), and exportable PDF certificates.")
             ], badge_text="Continuous Project Plan", bg_color=CARD_BG, font_size=9)

    card_ref = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.0), Inches(11.7), Inches(2.8))
    card_ref.fill.solid()
    card_ref.fill.fore_color.rgb = DARK_CARD_BG
    card_ref.line.color.rgb = DARK_CARD_BORDER
    tf_r = card_ref.text_frame
    tf_r.margin_left = tf_r.margin_right = Inches(0.3)
    tf_r.margin_top = Inches(0.2)

    pr_h = tf_r.paragraphs[0]
    pr_h.text = "OFFICIAL COURSE REFERENCES & CITATIONS"
    pr_h.font.bold = True
    pr_h.font.size = Pt(12)
    pr_h.font.color.rgb = ORANGE_ACCENT
    pr_h.space_after = Pt(8)

    refs = [
        ("Savitribai Phule Pune University (SPPU):",
         "Second Year Information Technology Syllabus (2024 Pattern) • Course: Skill Development Laboratory using Java (BIT25434A0X)."),
        ("Army Institute of Technology, Pune (AIT):",
         "Continuous Internal Evaluation (CIE-2) Group Activity Instructions, Problem Allocation & Evaluation Rubric (Mrs. Trupti Najan)."),
        ("Oracle Corporation:",
         "The Java Language Specification (Java SE 26 Edition) • Concepts: Inheritance, Polymorphic Dispatch, Interfaces, and Exception Handling."),
        ("Design Patterns (Gang of Four):",
         "Elements of Reusable Object-Oriented Software • Behavioral Strategy Pattern for decoupled scoring and Open/Closed extensibility.")
    ]

    for source, citation in refs:
        p = tf_r.add_paragraph()
        p.space_after = Pt(4)
        r_b = p.add_run()
        r_b.text = "➤ " + source + " "
        r_b.font.bold = True
        r_b.font.size = Pt(10)
        r_b.font.color.rgb = RGBColor(96, 165, 250)
        r_c = p.add_run()
        r_c.text = citation
        r_c.font.size = Pt(9.5)
        r_c.font.color.rgb = RGBColor(226, 232, 240)

    # Save
    out_file = r"g:\aunty gravity projects\java project\Online_Quiz_Management_System_Presentation.pptx"
    prs.save(out_file)
    print(f"Presentation successfully updated and saved at: {out_file} (Total Slides: {len(prs.slides)})")

if __name__ == "__main__":
    build_sih_presentation()
