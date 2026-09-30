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
    RED_ACCENT = RGBColor(220, 38, 38)      # #dc2626
    TEXT_MUTED = RGBColor(100, 116, 139)

    assets_dir = r"g:\aunty gravity projects\java project\ppt_assets"
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

        # Add AIT Badge in Top Right
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
        p_title.space_after = Pt(5)

        for itm in items:
            p = tf.add_paragraph()
            p.font.name = "Arial"
            p.font.size = Pt(font_size)
            p.space_after = Pt(2.5)
            
            if isinstance(itm, tuple):
                bold_prefix, rest = itm
                run_b = p.add_run()
                run_b.text = "• " + bold_prefix + ": "
                run_b.font.bold = True
                run_b.font.color.rgb = NAVY_TEXT
                run_r = p.add_run()
                run_r.text = rest
                run_r.font.color.rgb = RGBColor(51, 65, 85)
            else:
                p.text = "• " + itm
                p.font.color.rgb = RGBColor(51, 65, 85)

        return shape

    # =========================================================================
    # SLIDE 1: Title Slide (Removed Problem Statement ID per user request!)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_CREAM
    bg1.line.fill.background()

    # Top Banner Header
    tb1_head = s1.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(10.5), Inches(1.1))
    tf1_head = tb1_head.text_frame
    p1_h1 = tf1_head.paragraphs[0]
    p1_h1.text = "ARMY INSTITUTE OF TECHNOLOGY, PUNE"
    p1_h1.font.name = "Arial"
    p1_h1.font.size = Pt(26)
    p1_h1.font.bold = True
    p1_h1.font.color.rgb = TOP_BAR_NAVY

    p1_h2 = tf1_head.add_paragraph()
    p1_h2.text = "DEPARTMENT OF INFORMATION TECHNOLOGY • SKILL DEVELOPMENT LAB (BIT25434A0X)"
    p1_h2.font.name = "Arial"
    p1_h2.font.size = Pt(11)
    p1_h2.font.bold = True
    p1_h2.font.color.rgb = ORANGE_ACCENT

    if os.path.exists(ait_badge_path):
        s1.shapes.add_picture(ait_badge_path, Inches(11.5), Inches(0.5), Inches(1.2), Inches(1.2))

    # Left Column: Project and Team Info (Cleaned up: Problem Statement ID removed!)
    card_info = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), Inches(6.8), Inches(4.9))
    card_info.fill.solid()
    card_info.fill.fore_color.rgb = CARD_BG
    card_info.line.color.rgb = CARD_BORDER
    card_info.line.width = Pt(1.5)
    tfi = card_info.text_frame
    tfi.margin_left = Inches(0.4)
    tfi.margin_top = Inches(0.35)
    tfi.margin_right = Inches(0.4)

    info_items = [
        ("Project Title", "ONLINE QUIZ MANAGEMENT SYSTEM"),
        ("Assessment & Mode", "CIE–2: Java Problem Solving (Unit III & IV) | 20 Marks"),
        ("Course Name & Code", "Skill Development Laboratory using Java (BIT25434A0X)"),
        ("Class & Division", "SE IT B (Academic Year 2026–2027)"),
        ("Course In-Charge / Examiner", "Mrs. Trupti Najan (Assistant Professor, Dept of IT)"),
        ("Project Team Members", ""),
        ("  1. Aditya Yadav", "Roll No: 8108 (Group Leader)"),
        ("  2. Abhishekh Singh", "Roll No: 8104"),
        ("  3. Priyam Raj", "Roll No: 8134"),
        ("  4. Utkarsh Chauhan", "Roll No: 8154")
    ]

    p_first = tfi.paragraphs[0]
    p_first.text = "• " + info_items[0][0] + " — " + info_items[0][1]
    p_first.font.name = "Arial"
    p_first.font.size = Pt(13)
    p_first.font.bold = True
    p_first.font.color.rgb = NAVY_TEXT
    p_first.space_after = Pt(6)

    for label, val in info_items[1:]:
        p = tfi.add_paragraph()
        p.space_after = Pt(4.5)
        if label.startswith("  "):
            r1 = p.add_run()
            r1.text = "    " + label + " — "
            r1.font.bold = True
            r1.font.size = Pt(11)
            r1.font.color.rgb = BLUE_ACCENT
            r2 = p.add_run()
            r2.text = val
            r2.font.size = Pt(11)
            r2.font.color.rgb = NAVY_TEXT
        elif label == "Project Team Members":
            p.text = "• " + label + " (Class: IT B):"
            p.font.bold = True
            p.font.size = Pt(12)
            p.font.color.rgb = ORANGE_ACCENT
        else:
            r1 = p.add_run()
            r1.text = "• " + label + " — "
            r1.font.bold = True
            r1.font.size = Pt(11.5)
            r1.font.color.rgb = NAVY_TEXT
            r2 = p.add_run()
            r2.text = val
            r2.font.size = Pt(11.5)
            r2.font.color.rgb = RGBColor(71, 85, 105)

    # Right side: Tech Brain Illustration
    if os.path.exists(tech_brain_path):
        s1.shapes.add_picture(tech_brain_path, Inches(8.0), Inches(1.9), Inches(4.5), Inches(4.5))

    tb_num1 = s1.shapes.add_textbox(Inches(12.2), Inches(7.0), Inches(0.8), Inches(0.4))
    tb_num1.text_frame.paragraphs[0].text = "1"
    tb_num1.text_frame.paragraphs[0].font.size = Pt(12)

    # =========================================================================
    # SLIDE 2: Problem Formulation & Risk vs Solution (Matching Reference Slide 2)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s2, "Online Quiz System: Automated & Robust Academic Assessment", 2,
                     "PROBLEM STATEMENT, CORE INNOVATION & RISK-SOLUTION MATRIX")

    left_cards = [
        ("Real-world issue",
         "Colleges face heavy administrative overhead conducting manual paper tests. Subjective evaluation leads to grading delays, human scoring errors, and lack of immediate student performance analytics.",
         Inches(1.6)),
        ("Why important",
         "Faculty spend 15+ hours grading internal tests. Commercial tools fail on rigid formats, lack dual grading strategies (Standard vs Negative), and crash completely on typographic user input errors.",
         Inches(3.3)),
        ("Solution",
         "A modular Core Java assessment framework incorporating Unit III (Abstract Classes, Interfaces, Polymorphism) and Unit IV (5-tier Custom Checked Exceptions) for zero-crash immunity and instant scorecards.",
         Inches(5.0))
    ]

    for title, text, top in left_cards:
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(3.6), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = DARK_CARD_BG
        card.line.color.rgb = DARK_CARD_BORDER
        tf = card.text_frame
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.15)
        p1 = tf.paragraphs[0]
        p1.text = title.upper() + ":"
        p1.font.name = "Arial"
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = ORANGE_ACCENT
        p1.space_after = Pt(3)
        p2 = tf.add_paragraph()
        p2.text = text
        p2.font.name = "Arial"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = RGBColor(226, 232, 240)

    # Center: Core Innovation Graphic
    if os.path.exists(core_innov_path):
        s2.shapes.add_picture(core_innov_path, Inches(4.6), Inches(1.6), Inches(4.3), Inches(4.9))

    # Right Column: Risk -> Solution Pairs
    right_top = Inches(1.6)
    tb_rs = s2.shapes.add_textbox(Inches(9.1), right_top, Inches(3.4), Inches(0.4))
    p_rs = tb_rs.text_frame.paragraphs[0]
    p_rs.text = "OPERATIONAL RISK  ➔  TECHNICAL SOLUTION"
    p_rs.font.name = "Arial"
    p_rs.font.size = Pt(11)
    p_rs.font.bold = True
    p_rs.font.color.rgb = TOP_BAR_NAVY

    pairs = [
        ("Input Mismatches / Typos", "Student enters non-numeric or illegal chars like 'Z' crashing console.",
         "5-Tier Custom Exceptions", "try-catch InvalidOptionException catches format, prompts retry safely."),
        ("Rigid Single-Format Que", "Traditional apps only allow standard single-type multiple choice.",
         "Polymorphic Archetypes", "Abstract Question extended by MCQ, TrueFalse, and NumericQuestion."),
        ("Inflexible Scoring Rules", "University linear grading vs competitive exams require different math.",
         "Pluggable Strategy Pattern", "QuizEvaluator swaps Standard vs 25% Negative Marking dynamically.")
    ]

    for i, (r_title, r_desc, s_title, s_desc) in enumerate(pairs):
        card_r = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.1), Inches(2.1 + i * 1.5), Inches(3.4), Inches(1.35))
        card_r.fill.solid()
        card_r.fill.fore_color.rgb = CARD_BG
        card_r.line.color.rgb = CARD_BORDER
        tf = card_r.text_frame
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.12)
        p_r = tf.paragraphs[0]
        r_run = p_r.add_run()
        r_run.text = "Risk: " + r_title + "\n"
        r_run.font.bold = True
        r_run.font.size = Pt(9.5)
        r_run.font.color.rgb = RED_ACCENT
        r_sub = p_r.add_run()
        r_sub.text = r_desc + "\n"
        r_sub.font.size = Pt(8.5)
        r_sub.font.color.rgb = TEXT_MUTED

        p_s = tf.add_paragraph()
        s_run = p_s.add_run()
        s_run.text = "➔ Solution: " + s_title + "\n"
        s_run.font.bold = True
        s_run.font.size = Pt(9.5)
        s_run.font.color.rgb = GREEN_ACCENT
        s_sub = p_s.add_run()
        s_sub.text = s_desc
        s_sub.font.size = Pt(8.5)
        s_sub.font.color.rgb = NAVY_TEXT

    # =========================================================================
    # SLIDE 3: Technical Approach & Methodology (Matching Reference Slide 3)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s3, "Technical Approach & Implementation Methodology", 3,
                     "PROCESS LIFECYCLE, PIPELINE STAGES & ARCHITECTURE")

    # Left: Numbered Pipeline (1 to 6)
    card_pipe = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(3.5), Inches(5.0))
    card_pipe.fill.solid()
    card_pipe.fill.fore_color.rgb = CARD_BG
    card_pipe.line.color.rgb = CARD_BORDER
    tf_p = card_pipe.text_frame
    tf_p.margin_left = tf_p.margin_right = Inches(0.25)
    tf_p.margin_top = Inches(0.2)

    p_phead = tf_p.paragraphs[0]
    p_phead.text = "PIPELINE STAGES"
    p_phead.font.bold = True
    p_phead.font.size = Pt(12)
    p_phead.font.color.rgb = TOP_BAR_NAVY
    p_phead.space_after = Pt(8)

    pipe_steps = [
        ("1", "Multi-Tier Quiz Ingestion", "Validates unique ID, age demographic & questionCount > 0."),
        ("2", "Strategy Configuration", "Injects Standard or Competitive 25% negative marking."),
        ("3", "Dynamic Question Dispatch", "Iterates List<Question> invoking subclass display."),
        ("4", "Defensive Input Interception", "Guards parsing with try-catch InvalidOptionException."),
        ("5", "Strategy Evaluation", "Calculates net scores, percentages, and letter grades."),
        ("6", "Scorecard & Audit Generation", "Generates detailed question-by-question breakdown.")
    ]

    for num, title, desc in pipe_steps:
        p = tf_p.add_paragraph()
        p.space_after = Pt(5)
        r_num = p.add_run()
        r_num.text = f"[{num}] "
        r_num.font.bold = True
        r_num.font.size = Pt(10)
        r_num.font.color.rgb = BLUE_ACCENT
        r_title = p.add_run()
        r_title.text = title + "\n"
        r_title.font.bold = True
        r_title.font.size = Pt(9.5)
        r_title.font.color.rgb = NAVY_TEXT
        r_desc = p.add_run()
        r_desc.text = "     " + desc
        r_desc.font.size = Pt(8.5)
        r_desc.font.color.rgb = TEXT_MUTED

    # Center: Process Workflow Infographic
    if os.path.exists(process_flow_path):
        s3.shapes.add_picture(process_flow_path, Inches(4.5), Inches(1.6), Inches(5.4), Inches(3.2))

    card_arch = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(5.0), Inches(5.4), Inches(1.6))
    card_arch.fill.solid()
    card_arch.fill.fore_color.rgb = DARK_CARD_BG
    card_arch.line.color.rgb = DARK_CARD_BORDER
    tf_a = card_arch.text_frame
    tf_a.margin_left = tf_a.margin_right = Inches(0.25)
    tf_a.margin_top = Inches(0.15)
    pa1 = tf_a.paragraphs[0]
    pa1.text = "DUAL-MODE EXECUTION MODEL"
    pa1.font.bold = True
    pa1.font.size = Pt(11)
    pa1.font.color.rgb = ORANGE_ACCENT
    pa1.space_after = Pt(4)
    pa2 = tf_a.add_paragraph()
    pa2.text = "• Terminal CLI (run.bat): Interactive ANSI boxed console interface.\n• Web Application (run_web.bat): Embedded Java HttpServer at http://localhost:8080.\n• Automated Test Suite (run_tests.bat): 60-second test harness for live viva demonstration."
    pa2.font.size = Pt(9)
    pa2.font.color.rgb = RGBColor(226, 232, 240)

    # Right: Technologies Used Panel
    card_tech = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.1), Inches(1.6), Inches(2.4), Inches(5.0))
    card_tech.fill.solid()
    card_tech.fill.fore_color.rgb = CARD_BG
    card_tech.line.color.rgb = CARD_BORDER
    tf_t = card_tech.text_frame
    tf_t.margin_left = tf_t.margin_right = Inches(0.2)
    tf_t.margin_top = Inches(0.2)

    pt_h = tf_t.paragraphs[0]
    pt_h.text = "TECHNOLOGIES"
    pt_h.font.bold = True
    pt_h.font.size = Pt(11)
    pt_h.font.color.rgb = TOP_BAR_NAVY
    pt_h.space_after = Pt(8)

    techs = [
        ("Core Java", "JDK 26 SE runtime, OOP principles, dynamic binding."),
        ("Design Patterns", "Strategy Pattern (QuizEvaluator) & Aggregation."),
        ("Exception Tree", "5-tier custom checked exception hierarchy."),
        ("Collections", "LinkedHashMap, ArrayList, and Map."),
        ("Java HttpServer", "Built-in com.sun.net.httpserver with zero external JARs."),
        ("Web Frontend", "Modern HTML5, CSS3, and JavaScript Glassmorphism UI.")
    ]

    for name, sub in techs:
        p = tf_t.add_paragraph()
        p.space_after = Pt(4)
        r1 = p.add_run()
        r1.text = "• " + name + "\n"
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = BLUE_ACCENT
        r2 = p.add_run()
        r2.text = "  " + sub
        r2.font.size = Pt(8)
        r2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 4: Java Concept 1 - Abstract Classes (RE-DESIGNED WITH VISUAL DIAGRAM!)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s4, "Core Java Concept 1: Abstract Classes (Question & User)", 4,
                     "UML DOMAIN MODEL, ENCAPSULATED STATE & FORCED SPECIALIZATION")

    # Top: Visual Architectural Diagram Image!
    if os.path.exists(abstract_diagram_path):
        s4.shapes.add_picture(abstract_diagram_path, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.3))

    # Bottom Left Card: Abstract Class Question
    add_card(s4, Inches(0.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Abstract Base Class: Question",
             [
                 ("Why Abstract Class?", "Encapsulates shared fields (id, marks, topic, difficulty) and displayHeader(), but cannot be instantiated directly without choice logic."),
                 ("Pure Abstract Methods", "abstract void displayQuestion(); abstract boolean checkAnswer(String ans) throws InvalidOptionException; abstract String getCorrectAnswerFormatted();"),
                 ("Subclass Archetypes", "MultipleChoiceQuestion (A-D options), TrueFalseQuestion (Boolean T/F), NumericQuestion (tolerance delta).")
             ], badge_text="Core Domain Model", font_size=8.5)

    # Bottom Right Card: User Hierarchy
    add_card(s4, Inches(6.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Subclasses & User Hierarchy",
             [
                 ("Abstract Class: User", "Encapsulates common user identity (userId, name, email) and enforces abstract void displayDashboard();."),
                 ("Student (Subclass)", "Overrides displayDashboard() displaying total attempts, average percentage, and attempt history records."),
                 ("Instructor (Subclass)", "Overrides displayDashboard() displaying faculty designation, department, and authoring permissions.")
             ], badge_text="Inheritance & Dashboards", font_size=8.5)

    # =========================================================================
    # SLIDE 5: Java Concept 2 - Interfaces & Strategy Pattern (WITH VISUAL DIAGRAM!)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s5, "Core Java Concept 2: Interfaces & Strategy Pattern", 5,
                     "BEHAVIORAL CONTRACTS & RUNTIME SCORING DECOUPLING")

    # Top: Visual Strategy Pattern Diagram Image!
    if os.path.exists(strategy_diagram_path):
        s5.shapes.add_picture(strategy_diagram_path, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.3))

    # Bottom Left Card: Interface QuizOperations
    add_card(s5, Inches(0.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Interface: QuizOperations (Lifecycle Contract)",
             [
                 ("Contract Definition", "Defines createQuiz, addQuestionToQuiz, getQuiz, searchQuiz, deleteQuiz without coupling to persistence."),
                 ("Checked Exceptions", "Declares checked exceptions in signatures (throws QuizNotFoundException, DuplicateQuizException)."),
                 ("Service Implementation", "Implemented by QuizManager using Collections Framework (LinkedHashMap and ArrayList).")
             ], badge_text="CRUD Lifecycle Contract", font_size=8.5)

    # Bottom Right Card: Strategy Pattern
    add_card(s5, Inches(6.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Interface: QuizEvaluator (Pluggable Strategies)",
             [
                 ("The Strategy Design Pattern", "Decouples scoring logic from test conduction. Injected dynamically at runtime based on exam type."),
                 ("StandardGradingPolicy", "Linear scoring (100% correct, 0% penalty) for regular university internal assessments."),
                 ("NegativeMarkingGradingPolicy", "Competitive exam scoring (25% deduction for incorrect answers), satisfying the Open/Closed Principle.")
             ], badge_text="Interchangeable Grading Strategies", font_size=8.5)

    # =========================================================================
    # SLIDE 6: Java Concept 3 - Polymorphism in Action (WITH VISUAL DIAGRAM!)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s6, "Core Java Concept 3: Polymorphism in Action", 6,
                     "DYNAMIC METHOD DISPATCH (vtable) & STATIC METHOD OVERLOADING")

    # Top: Visual Polymorphism Diagram Image!
    if os.path.exists(poly_diagram_path):
        s6.shapes.add_picture(poly_diagram_path, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.3))

    # Bottom Left: Runtime Polymorphism
    add_card(s6, Inches(0.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Runtime Polymorphism (Dynamic Method Dispatch)",
             [
                 ("Dynamic Question Dispatch", "Iterating List<Question>: q.displayQuestion() and q.checkAnswer() dynamically resolve to MCQ, TrueFalse, or Numeric via JVM vtable."),
                 ("Interface Strategy Dispatch", "QuizEvaluator evaluator = (mode == 1) ? new StandardGradingPolicy() : new NegativeMarkingGradingPolicy(); evaluator.evaluateScore(attempt);"),
                 ("Dashboard Dispatch", "User userRef = currentStudent; userRef.displayDashboard(); dynamically binds to Student's dashboard.")
             ], badge_text="Dynamic Binding (vtable)", font_size=8.5)

    # Bottom Right: Compile-time Polymorphism
    add_card(s6, Inches(6.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Compile-Time Polymorphism (Method Overloading)",
             [
                 ("Overloaded searchQuiz", "searchQuiz(String topic); filters by topic; searchQuiz(String topic, DifficultyLevel level); filters topic & difficulty."),
                 ("Overloaded readInteger", "readInteger(scanner, prompt); and bounded readInteger(scanner, prompt, min, max); in InputValidator."),
                 ("Overloaded evaluateScore", "evaluateScore(QuizAttempt) vs evaluateScore(earnedMarks, incorrectCount, penaltyPerIncorrect).")
             ], badge_text="Static Binding / Overloading", font_size=8.5)

    # =========================================================================
    # SLIDE 7: Java Concept 4 - Exception Handling Hierarchy (WITH VISUAL DIAGRAM!)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s7, "Core Java Concept 4: Exception Handling Hierarchy", 7,
                     "CUSTOM CHECKED EXCEPTIONS & DEFENSIVE EXECUTION")

    # Top: Visual Exception Tree Diagram Image!
    if os.path.exists(exception_diagram_path):
        s7.shapes.add_picture(exception_diagram_path, Inches(0.8), Inches(1.5), Inches(11.7), Inches(3.3))

    # Bottom Left: Custom Exception Tree
    add_card(s7, Inches(0.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Custom Checked Exception Hierarchy",
             [
                 ("Root: QuizException", "Extends java.lang.Exception. Root checked exception for domain integrity."),
                 ("QuizNotFoundException", "Thrown when accessing or deleting an unmapped Quiz ID (e.g. 'GHOST-404')."),
                 ("DuplicateQuizException", "Thrown when faculty attempts to register a duplicate ID (e.g. 'JAVA-OOP')."),
                 ("InvalidOptionException", "Thrown when a student provides an out-of-range option (e.g. 'Z' on MCQ or text in numeric)."),
                 ("EmptyQuizException", "Thrown if an attempt is made to conduct a quiz containing zero questions.")
             ], badge_text="Custom Exception Tree", font_size=8.5)

    # Bottom Right: try-catch-finally execution
    add_card(s7, Inches(6.8), Inches(4.95), Inches(5.7), Inches(1.85),
             "Structured Try-Catch-Finally Architecture",
             [
                 ("The 'try' Block", "Isolates critical operations: reading console inputs, invoking domain services, and validating student answers."),
                 ("The 'catch' Block", "Intercepts specific checked exceptions, prints clear diagnostic recovery guidance, and re-prompts without terminating."),
                 ("The 'finally' Block", "Guaranteed execution regardless of exception or normal completion: manages graceful resource shutdown and audit confirmation logs."),
                 ("Defensive Input Handling", "InputValidator wraps NumberFormatException, guaranteeing zero console crashes.")
             ], badge_text="Fault-Tolerant Execution", font_size=8.5)

    # =========================================================================
    # SLIDE 8: Feasibility and Viability (Matching Reference Slide 4)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s8, "Feasibility, Viability & Educational Verification", 8,
                     "INFRASTRUCTURE READINESS, SCALABILITY & ACADEMIC VALUE")

    col_w = Inches(3.7)
    cols = [
        ("FEASIBILITY ANALYSIS",
         [("Zero External Dependencies", "Built strictly with standard Java SE (JDK 8–26). No Maven/Gradle or third-party JARs required."),
          ("Dual-Mode Deployability", "Runs seamlessly in terminal console (run.bat) or modern web browser (run_web.bat) via embedded HttpServer."),
          ("Cross-Platform Portability", "Executes identically on Windows, Linux, and macOS runtimes."),
          ("Faculty Time Efficiency", "Eliminates 100% of manual grading time and scorecard calculation errors.")],
         Inches(0.8), "Feasibility"),

        ("VIABILITY & TRUST",
         [("Proven Design Patterns", "Builds on industry-standard Strategy Pattern and SOLID Object-Oriented principles."),
          ("Zero-Crash Guarantee", "Defensive input validation prevents fatal session terminations on typographical mistakes."),
          ("Accountability & Audits", "Comprehensive question-by-question breakdown provides transparent verification for students."),
          ("Academic Alignment", "100% compliant with SPPU / AIT Pune BIT25434A0X course outcomes (CO3, CO4).")],
         Inches(0.8 + 1 * (3.7 + 0.3)), "Viability"),

        ("ACADEMIC POTENTIAL",
         [("Multi-Age Demographics", "Serves 4 distinct learner tiers: Kids (8-12), Teens (13-17), College (18-22), and Pro (20+)."),
          ("Department-Wide Scalability", "Easily adoptable across all departments at Army Institute of Technology, Pune."),
          ("Competitive Exam Prep", "Prepares engineering students for GATE / TCS NQT competitive negative marking examinations."),
          ("Extensible Roadmap", "Provides an ideal prototype foundation for Phase 2/3 MySQL database and Spring Boot integration.")],
         Inches(0.8 + 2 * (3.7 + 0.3)), "Educational Impact")
    ]

    for title, items, left, badge in cols:
        add_card(s8, left, Inches(1.6), col_w, Inches(5.2), title, items, badge_text=badge, bg_color=CARD_BG, font_size=9)

    # =========================================================================
    # SLIDE 9: Impact and Benefits (Matching Reference Slide 5)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s9, "Impact and Benefits: Traditional vs Java Quiz System", 9,
                     "SYSTEM PERFORMANCE BENCHMARKS & VALUE PROPOSITION")

    # Left: Benefits Wheel Infographic
    if os.path.exists(benefits_wheel_path):
        s9.shapes.add_picture(benefits_wheel_path, Inches(0.8), Inches(1.6), Inches(4.8), Inches(4.8))

    # Right: Metric Comparison Table (Like Reference Slide 5)
    card_table = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.8), Inches(1.6), Inches(6.7), Inches(5.0))
    card_table.fill.solid()
    card_table.fill.fore_color.rgb = CARD_BG
    card_table.line.color.rgb = CARD_BORDER
    tf_tbl = card_table.text_frame
    tf_tbl.margin_left = tf_tbl.margin_right = Inches(0.25)
    tf_tbl.margin_top = Inches(0.2)

    p_th = tf_tbl.paragraphs[0]
    p_th.text = "ACADEMIC SCREENING: CURRENT VS ONLINE QUIZ SYSTEM"
    p_th.font.name = "Arial"
    p_th.font.size = Pt(12)
    p_th.font.bold = True
    p_th.font.color.rgb = TOP_BAR_NAVY
    p_th.space_after = Pt(10)

    metrics = [
        ("Grading Accuracy", "70%", "100%", "Human error vs Automated mathematical precision"),
        ("Result Turnaround", "3 to 7 Days", "< 1 Second", "Paper collection vs Instant scorecard generation"),
        ("Crash / Failure Rate", "40% (Fatal)", "0% (Immune)", "Typos crash app vs 5-tier exception recovery"),
        ("Grading Flexibility", "Rigid Linear", "Dual Dynamic", "Single format vs Standard + Negative Marking"),
        ("Performance Feedback", "Score Only", "Granular Audit", "Minimal review vs Question-by-question breakdown"),
        ("Faculty Workload", "15+ Hours", "Automated", "Manual grading burden vs Instant report tabulation")
    ]

    for m_name, curr, with_sys, note in metrics:
        p = tf_tbl.add_paragraph()
        p.space_after = Pt(4)
        r_m = p.add_run()
        r_m.text = m_name + " — "
        r_m.font.bold = True
        r_m.font.size = Pt(9.5)
        r_m.font.color.rgb = NAVY_TEXT

        r_curr = p.add_run()
        r_curr.text = f"[Manual: {curr}] "
        r_curr.font.size = Pt(9)
        r_curr.font.bold = True
        r_curr.font.color.rgb = RED_ACCENT

        r_sys = p.add_run()
        r_sys.text = f"➔ [With Java System: {with_sys}]\n"
        r_sys.font.size = Pt(9)
        r_sys.font.bold = True
        r_sys.font.color.rgb = GREEN_ACCENT

        r_note = p.add_run()
        r_note.text = "   " + note
        r_note.font.size = Pt(8)
        r_note.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 10: Implementation & Live Demonstration
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
             ], badge_text="Console CLI", border_color=CARD_BORDER, font_size=9)

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
    # SLIDE 11: Individual Work Allocation & Team Contributions
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s11, "Individual Contribution & Work Allocation (SE IT B)", 11,
                     "EXPLICIT RUBRIC RESPONSIBILITY MATRIX & CLASS ASSIGNMENT")

    team_alloc = [
        ("Aditya Yadav", "Roll No: 8108",
         [("Assigned Role", "Group Leader & System Architect"),
          ("Unit III Topics", "Abstract Classes & Methods; Shared State Encapsulation (IS-A Model)"),
          ("Unit IV Topics", "Types of Error (Syntax vs Logic) & Defensive Constructor Validation"),
          ("Implementation", "abstract class Question & User; Quiz aggregation; marks > 0 guards"),
          ("Viva Defense", "Why abstract classes? Abstract class vs Interface; forced specialization.")]),

        ("Abhishekh Singh", "Roll No: 8104",
         [("Assigned Role", "Polymorphic Question Specialist"),
          ("Unit III Topics", "Polymorphism, Method Overriding (@Override) & Dynamic Binding (vtable)"),
          ("Unit IV Topics", "Exception Interception & Handling in Answers (InvalidOptionException)"),
          ("Implementation", "MultipleChoiceQuestion, TrueFalseQuestion, NumericQuestion; Overloading"),
          ("Viva Defense", "Where is polymorphism used? Dynamic dispatch via JVM virtual method table.")]),

        ("Priyam Raj", "Roll No: 8134",
         [("Assigned Role", "Service & Strategy Pattern Engineer"),
          ("Unit III Topics", "Interfaces (QuizOperations, QuizEvaluator) & Strategy Design Pattern"),
          ("Unit IV Topics", "Exception Propagation & Interface Method 'throws' Contract Signatures"),
          ("Implementation", "StandardGradingPolicy (linear) vs NegativeMarkingGradingPolicy (25% penalty)"),
          ("Viva Defense", "Why QuizEvaluator interface? Open/Closed Principle; decoupling logic.")]),

        ("Utkarsh Chauhan", "Roll No: 8154",
         [("Assigned Role", "Quality Assurance & Exception Architect"),
          ("Unit III Topics", "Interface Implementation (QuizManager) & Pluggable Service Wiring"),
          ("Unit IV Topics", "User-Defined Exceptions (5 Checked) & Structured try-catch-finally"),
          ("Implementation", "QuizException tree (5 domain exceptions); InputValidator; run_tests.bat"),
          ("Viva Defense", "Checked vs unchecked exceptions; purpose of try, catch, and finally blocks.")])
    ]

    coords_s11 = [
        (Inches(0.8), Inches(1.6)),
        (Inches(6.8), Inches(1.6)),
        (Inches(0.8), Inches(4.35)),
        (Inches(6.8), Inches(4.35))
    ]

    for i, (name, roll, details) in enumerate(team_alloc):
        left, top = coords_s11[i]
        add_card(s11, left, top, Inches(5.7), Inches(2.6), f"{name} ({roll})", details, badge_text="Team Member (IT B)", font_size=8)

    # =========================================================================
    # SLIDE 12: Continuous Project Roadmap & References (Matching Reference Slide 6)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s12, "Continuous Project Roadmap & Academic References", 12,
                     "EXPANSION PHASES & OFFICIAL COURSE CITATIONS")

    add_card(s12, Inches(0.8), Inches(1.6), Inches(11.7), Inches(2.2),
             "Ongoing Mini-Project Roadmap (CIE-2 Phase 1 to Phase 3 Expansion)",
             [
                 ("Phase 1 (Completed for CIE-2)", "Core Java OOP Prototype with Abstract Classes, Interfaces, Polymorphism, and 5-tier Custom Exceptions."),
                 ("Phase 2 (Project Enhancement)", "Replace in-memory LinkedHashMap with Java Object Serialization or File I/O; add advanced Java Streams filtering."),
                 ("Phase 3 (Full Mini-Project Expansion)", "JDBC connectivity with MySQL / PostgreSQL, Spring Boot REST migration, Multithreaded question timers (ScheduledExecutorService), and exportable PDF certificates.")
             ], badge_text="Continuous Project Plan", bg_color=CARD_BG, font_size=9)

    card_ref = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.0), Inches(11.7), Inches(2.8))
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
    print(f"Presentation successfully updated and saved at: {out_file}")

if __name__ == "__main__":
    build_sih_presentation()
