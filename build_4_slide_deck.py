import os
import subprocess
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_4_slide_presentation():
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
    TOP_BAR_NAVY = RGBColor(27, 54, 93)     # #1b365d navy
    NAVY_TEXT = RGBColor(15, 23, 42)        # #0f172a
    CARD_BG = RGBColor(255, 255, 255)       # white
    CARD_BORDER = RGBColor(226, 232, 240)   # soft border
    DARK_CARD_BG = RGBColor(30, 41, 59)     # dark blue card
    DARK_CARD_BORDER = RGBColor(51, 65, 85)
    ORANGE_ACCENT = RGBColor(234, 88, 12)   # #ea580c
    GREEN_ACCENT = RGBColor(22, 163, 74)    # #16a34a
    BLUE_ACCENT = RGBColor(37, 99, 235)     # #2563eb
    PURPLE_ACCENT = RGBColor(147, 51, 234)  # #9333ea
    CYAN_ACCENT = RGBColor(8, 145, 178)     # #0891b2
    RED_ACCENT = RGBColor(220, 38, 38)      # #dc2626
    TEXT_MUTED = RGBColor(100, 116, 139)

    base_dir = r"g:\aunty gravity projects\java project"
    assets_dir = os.path.join(base_dir, "ppt_assets")
    ait_badge_path = os.path.join(assets_dir, "ait_badge.jpg")
    tech_brain_path = os.path.join(assets_dir, "quiz_tech_brain.jpg")
    core_innov_path = os.path.join(assets_dir, "quiz_core_innovation.jpg")
    process_flow_path = os.path.join(assets_dir, "quiz_process_workflow.jpg")
    benefits_wheel_path = os.path.join(assets_dir, "quiz_benefits_wheel.jpg")

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
        p.font.size = Pt(21)
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
        tb_num = slide.shapes.add_textbox(Inches(12.0), Inches(7.05), Inches(1.0), Inches(0.35))
        tf_num = tb_num.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.text = f"Slide {slide_num} of 4"
        p_num.font.name = "Arial"
        p_num.font.size = Pt(10)
        p_num.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, items, badge_text=None, border_color=CARD_BORDER, bg_color=CARD_BG, font_size=9):
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
        p_title.font.size = Pt(11.5)
        p_title.font.bold = True
        p_title.font.color.rgb = TOP_BAR_NAVY
        p_title.space_after = Pt(4)

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
    # SLIDE 1: TEAM NAME & MEMBERS (Title & Team Identification)
    # Strictly NO Problem Statement ID as requested
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = BG_CREAM
    bg1.line.fill.background()

    # Top Department Bar
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.04))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = TOP_BAR_NAVY
    top_bar.line.fill.background()

    # Institution & Evaluation Header
    tb_inst = s1.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(10.5), Inches(0.85))
    tf_inst = tb_inst.text_frame
    p_inst = tf_inst.paragraphs[0]
    p_inst.text = "ARMY INSTITUTE OF TECHNOLOGY (AIT), PUNE • DEPARTMENT OF IT"
    p_inst.font.name = "Arial"
    p_inst.font.size = Pt(13)
    p_inst.font.bold = True
    p_inst.font.color.rgb = TOP_BAR_NAVY

    p_eval = tf_inst.add_paragraph()
    p_eval.text = "Skill Development Laboratory using Java (BIT25434A0X) | Continuous Internal Evaluation 2 (CIE-2)"
    p_eval.font.name = "Arial"
    p_eval.font.size = Pt(11)
    p_eval.font.bold = True
    p_eval.font.color.rgb = ORANGE_ACCENT

    # Add Crest Badge
    if os.path.exists(ait_badge_path):
        s1.shapes.add_picture(ait_badge_path, Inches(11.45), Inches(0.45), Inches(1.05), Inches(1.05))

    # Hero Project Title Banner
    hero_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.6))
    hero_card.fill.solid()
    hero_card.fill.fore_color.rgb = DARK_CARD_BG
    hero_card.line.color.rgb = DARK_CARD_BORDER
    hero_card.line.width = Pt(1.5)
    tf_hero = hero_card.text_frame
    tf_hero.margin_left = tf_hero.margin_right = Inches(0.35)
    tf_hero.margin_top = Inches(0.2)

    p_ht = tf_hero.paragraphs[0]
    p_ht.text = "ONLINE QUIZ MANAGEMENT SYSTEM"
    p_ht.font.name = "Arial"
    p_ht.font.size = Pt(26)
    p_ht.font.bold = True
    p_ht.font.color.rgb = RGBColor(255, 255, 255)

    p_hs = tf_hero.add_paragraph()
    p_hs.text = "A Fault-Tolerant, Dual-Grading Academic Assessment Platform in Java SE & Glassmorphism Web UI"
    p_hs.font.name = "Arial"
    p_hs.font.size = Pt(13)
    p_hs.font.color.rgb = RGBColor(226, 232, 240)
    p_hs.space_after = Pt(4)

    p_ex = tf_hero.add_paragraph()
    p_ex.text = "Class: SE IT B  •  Course In-charge / Examiner: Mrs. Trupti Najan  •  Academic Year: 2026"
    p_ex.font.name = "Arial"
    p_ex.font.size = Pt(11)
    p_ex.font.bold = True
    p_ex.font.color.rgb = ORANGE_ACCENT

    # Team Members Section Heading
    tb_th = s1.shapes.add_textbox(Inches(0.8), Inches(3.25), Inches(11.733), Inches(0.35))
    p_th = tb_th.text_frame.paragraphs[0]
    p_th.text = "PROJECT TEAM MEMBERS & WORK DISTRIBUTION"
    p_th.font.name = "Arial"
    p_th.font.size = Pt(12)
    p_th.font.bold = True
    p_th.font.color.rgb = TOP_BAR_NAVY

    # 4 Team Member Cards
    team_data = [
        ("Aditya Yadav", "8108", "GROUP LEADER",
         [("Role", "System Architect & Integration Lead"),
          ("Interfaces", "QuizOperations & QuizEvaluator contracts"),
          ("Patterns", "Strategy Pattern & Polymorphic binding"),
          ("Coordination", "Submission alignment & Rubric compliance")],
         ORANGE_ACCENT),

        ("Abhishekh Singh", "8104", "CORE DEVELOPER",
         [("Role", "OOP & Custom Exceptions Lead"),
          ("Abstract Classes", "Question & User base hierarchies"),
          ("Exception Tree", "5-tier checked QuizException hierarchy"),
          ("Archetypes", "MCQ, True/False & Numeric questions")],
         BLUE_ACCENT),

        ("Priyam Raj", "8134", "WEB DEVELOPER",
         [("Role", "Full-Stack Web & REST Engineer"),
          ("Server", "Embedded Java HttpServer on port 8080"),
          ("Client UI", "Responsive Glassmorphism Web App"),
          ("Timer & JSON", "Live 10-min countdown & REST APIs")],
         PURPLE_ACCENT),

        ("Utkarsh Chauhan", "8154", "QA & TESTING",
         [("Role", "Quality Assurance & Evaluation Lead"),
          ("Test Suite", "Automated CIE-2 viva demonstration harness"),
          ("Validation", "Standard vs 25% Negative Marking verification"),
          ("Defensive Code", "Zero-crash input interceptors & recovery")],
         GREEN_ACCENT)
    ]

    card_w = Inches(2.78)
    card_gap = Inches(0.2)
    card_top = Inches(3.65)
    card_h = Inches(2.8)

    for i, (name, roll, tag, duties, tag_color) in enumerate(team_data):
        c_left = Inches(0.8) + i * (card_w + card_gap)
        c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, card_top, card_w, card_h)
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = CARD_BORDER
        c.line.width = Pt(1.5)
        tf_c = c.text_frame
        tf_c.margin_left = tf_c.margin_right = Inches(0.18)
        tf_c.margin_top = Inches(0.16)

        p_tag = tf_c.paragraphs[0]
        p_tag.text = tag
        p_tag.font.name = "Arial"
        p_tag.font.size = Pt(8.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = tag_color
        p_tag.space_after = Pt(2)

        p_name = tf_c.add_paragraph()
        p_name.text = name
        p_name.font.name = "Arial"
        p_name.font.size = Pt(13)
        p_name.font.bold = True
        p_name.font.color.rgb = TOP_BAR_NAVY

        p_roll = tf_c.add_paragraph()
        p_roll.text = f"Roll No: {roll} • SE IT B"
        p_roll.font.name = "Arial"
        p_roll.font.size = Pt(9.5)
        p_roll.font.bold = True
        p_roll.font.color.rgb = TEXT_MUTED
        p_roll.space_after = Pt(5)

        for b_title, b_desc in duties:
            p_d = tf_c.add_paragraph()
            p_d.space_after = Pt(2)
            r_b = p_d.add_run()
            r_b.text = "• " + b_title + ": "
            r_b.font.name = "Arial"
            r_b.font.size = Pt(8.5)
            r_b.font.bold = True
            r_b.font.color.rgb = NAVY_TEXT
            r_r = p_d.add_run()
            r_r.text = b_desc
            r_r.font.name = "Arial"
            r_r.font.size = Pt(8.5)
            r_r.font.color.rgb = RGBColor(51, 65, 85)

    # Bottom Links Footer
    tb_foot = s1.shapes.add_textbox(Inches(0.8), Inches(6.6), Inches(11.733), Inches(0.45))
    tf_foot = tb_foot.text_frame
    p_ft = tf_foot.paragraphs[0]
    p_ft.text = "🌐 Live Interactive Portal: https://abhisheksinghapsb-gif.github.io/Online-Quiz-Management-System/   |   💻 GitHub: abhisheksinghapsb-gif/Online-Quiz-Management-System"
    p_ft.font.name = "Arial"
    p_ft.font.size = Pt(9.5)
    p_ft.font.bold = True
    p_ft.font.color.rgb = BLUE_ACCENT

    # =========================================================================
    # SLIDE 2: INTRODUCTION (Problem Statement, Motivation & 4 Java Pillars)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s2, "Introduction: Problem Context & Architectural Vision", 2,
                     "ACADEMIC MOTIVATION, SYSTEM OBJECTIVES & 4 CORE JAVA PILLARS")

    # Left Column: Problem vs Solution Cards
    col_w2 = Inches(3.6)
    left_x = Inches(0.8)

    add_card(s2, left_x, Inches(1.6), col_w2, Inches(2.4),
             "The Academic Challenge",
             [
                 ("Paper Exam Burden", "Manual test administration causes 15+ hours of grading overhead per exam."),
                 ("Turnaround Latency", "Students wait 3 to 7 days before receiving marks and actionable feedback."),
                 ("Human Scoring Errors", "Subjective evaluation leads to mathematical calculation discrepancies."),
                 ("Rigid Software Tools", "Traditional applications lack negative marking and crash on typographical input errors.")
             ], badge_text="Problem Formulation", border_color=CARD_BORDER, font_size=8.5)

    add_card(s2, left_x, Inches(4.2), col_w2, Inches(2.6),
             "Our Solution: Online Quiz System",
             [
                 ("Zero-Crash Architecture", "5-tier custom checked exception tree intercepts typos without fatal crashes."),
                 ("Dual Grading Strategies", "Instant runtime switch between Standard Linear and 25% Negative Marking."),
                 ("Automated Scorecards", "Immediate objective score computation, percentages, and letter grades."),
                 ("Multi-Age Repositories", "9 pre-loaded quizzes across 4 age demographics (Kids, Teens, College, Pro).")
             ], badge_text="Core Innovation", border_color=GREEN_ACCENT, font_size=8.5)

    # Center: Innovation Shield Graphic
    if os.path.exists(core_innov_path):
        s2.shapes.add_picture(core_innov_path, Inches(4.6), Inches(1.6), Inches(4.1), Inches(5.2))

    # Right Column: The 4 Core Java Pillars from Unit III & IV
    right_x = Inches(8.9)
    col_w_r = Inches(3.633)

    add_card(s2, right_x, Inches(1.6), col_w_r, Inches(5.2),
             "The 4 Mandatory Java Concepts",
             [
                 ("1. Abstract Classes (Unit III)",
                  "Question & User base hierarchies encapsulate shared fields (id, marks, topic) while forcing subclasses to implement specialized display and validation logic."),
                 ("2. Interfaces & Strategy (Unit III)",
                  "QuizEvaluator interface decouples scoring algorithms, enabling StandardGradingPolicy vs NegativeMarkingGradingPolicy without touching runner code."),
                 ("3. Polymorphism in Action (Unit III)",
                  "Runtime Dynamic Method Dispatch resolves MCQ, True/False, and Numeric questions on the fly. Compile-time Method Overloading provides multi-criteria search."),
                 ("4. Custom Exception Tree (Unit IV)",
                  "5-tier checked hierarchy (QuizException, QuizNotFound, DuplicateQuiz, InvalidOption, InvalidQuestion, EmptyQuiz) guarantees bulletproof crash immunity.")
             ], badge_text="Unit III & IV Compliance", border_color=BLUE_ACCENT, font_size=8.5)

    # =========================================================================
    # SLIDE 3: WORKING (Architecture, Execution Lifecycle & Delivery Modes)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s3, "System Working: Execution Lifecycle & Architecture", 3,
                     "5-STAGE ASSESSMENT PIPELINE, DYNAMIC DISPATCH & TRIPLE DELIVERY MODES")

    # Left Column: 5-Stage Execution Pipeline
    card_pipe = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2))
    card_pipe.fill.solid()
    card_pipe.fill.fore_color.rgb = CARD_BG
    card_pipe.line.color.rgb = CARD_BORDER
    tf_p = card_pipe.text_frame
    tf_p.margin_left = tf_p.margin_right = Inches(0.25)
    tf_p.margin_top = Inches(0.18)

    p_phead = tf_p.paragraphs[0]
    p_phead.text = "5-STAGE ASSESSMENT LIFECYCLE"
    p_phead.font.bold = True
    p_phead.font.size = Pt(11.5)
    p_phead.font.color.rgb = TOP_BAR_NAVY
    p_phead.space_after = Pt(6)

    pipe_steps = [
        ("1", "Multi-Tier Ingestion", "Validates unique Quiz ID, age category (Kids/Teens/College/Pro) & questionCount > 0."),
        ("2", "Strategy Injection", "Dynamically injects Standard Linear or 25% Competitive Negative Marking policy."),
        ("3", "Dynamic Dispatch", "Iterates List<Question> polymorphically, delegating to MCQ, TF, or Numeric subclasses."),
        ("4", "Defensive Interception", "Catches illegal user entries (e.g. typing 'Z') with InvalidOptionException for safe retry."),
        ("5", "Scorecard & Audit", "Evaluates net scores, percentages, letter grades (A+, A, B, C, F), and logs history.")
    ]

    for num, title, desc in pipe_steps:
        p = tf_p.add_paragraph()
        p.space_after = Pt(4)
        r_num = p.add_run()
        r_num.text = f"[{num}] "
        r_num.font.bold = True
        r_num.font.size = Pt(9.5)
        r_num.font.color.rgb = BLUE_ACCENT
        r_title = p.add_run()
        r_title.text = title + "\n"
        r_title.font.bold = True
        r_title.font.size = Pt(9)
        r_title.font.color.rgb = NAVY_TEXT
        r_desc = p.add_run()
        r_desc.text = "     " + desc
        r_desc.font.size = Pt(8)
        r_desc.font.color.rgb = TEXT_MUTED

    # Center: Process Flowchart Image
    if os.path.exists(process_flow_path):
        s3.shapes.add_picture(process_flow_path, Inches(4.7), Inches(1.6), Inches(4.3), Inches(3.3))

    # Center Bottom: Strategy Pattern Highlight Card
    card_strat = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.7), Inches(5.05), Inches(4.3), Inches(1.75))
    card_strat.fill.solid()
    card_strat.fill.fore_color.rgb = DARK_CARD_BG
    card_strat.line.color.rgb = DARK_CARD_BORDER
    tf_s = card_strat.text_frame
    tf_s.margin_left = tf_s.margin_right = Inches(0.2)
    tf_s.margin_top = Inches(0.14)

    ps1 = tf_s.paragraphs[0]
    ps1.text = "STRATEGY PATTERN (QuizEvaluator)"
    ps1.font.bold = True
    ps1.font.size = Pt(10.5)
    ps1.font.color.rgb = ORANGE_ACCENT
    ps1.space_after = Pt(3)

    ps2 = tf_s.add_paragraph()
    ps2.text = "• Standard Policy: Score = Sum of correct question marks.\n• Competitive Policy: Score = Correct - (0.25 * Incorrect Marks).\n• Decoupled Architecture: Zero runner modifications required to add new grading rules (Open/Closed Principle)."
    ps2.font.size = Pt(8.5)
    ps2.font.color.rgb = RGBColor(226, 232, 240)

    # Right Column: Triple Delivery Modes
    right_col = [
        ("Terminal CLI (run.bat)",
         [("Pure Core Java", "Works directly in Windows Command Prompt without external dependencies."),
          ("Interactive Menus", "Student & Faculty dashboards with formatted ASCII table views."),
          ("Zero-Crash Recovery", "Entering 'Z' triggers safe retry without terminating application.")],
         "Mode 1", Inches(1.6)),

        ("Modern Web UI (run_web.bat)",
         [("Embedded Server", "Lightweight Java HttpServer on port 8080 with zero external JARs."),
          ("Live Countdown", "10-minute automated quiz timer with radio options & score modals."),
          ("GitHub Pages", "Hosted live online for instant browser access without setup.")],
         "Mode 2", Inches(3.35)),

        ("Automated Viva Harness (run_tests.bat)",
         [("60-Second Proof", "Specially designed for the 8-10 minute CIE-2 viva demonstration."),
          ("All 4 Concepts", "Tests dynamic dispatch, strategy swapping, and overloaded searches."),
          ("Exception Traces", "Deliberately triggers and catches all 5 exceptions with finally blocks.")],
         "Mode 3", Inches(5.1))
    ]

    for title, items, badge, top_pos in right_col:
        add_card(s3, Inches(9.2), top_pos, Inches(3.333), Inches(1.65), title, items, badge_text=badge, border_color=CARD_BORDER, font_size=8)

    # =========================================================================
    # SLIDE 4: EXPLAINING THE UI OF WEBSITE (Interactive Web Portal)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_base_slide(s4, "Explaining the Website UI: Architecture & User Experience", 4,
                     "INTERACTIVE GLASSMORPHISM DASHBOARD, REAL-TIME TIMER & COMPONENT BREAKDOWN")

    # 6 Structured UI Component Cards (2 rows of 3 cards)
    ui_components = [
        # Row 1
        ("1. Institution Header & Navigation",
         [("Branding Crest", "AIT Pune crest & Department of IT badge with active CIE-2 examination status."),
          ("Persistent Nav Bar", "5-tab navigation: Quizzes, Active Quiz, Score History, Faculty, and Concept Defense."),
          ("Student Pill", "Displays active logged-in student name, roll number, and division in header.")],
         "Header & Navigation", Inches(0.8), Inches(1.6)),

        ("2. Interactive Filter & Search Bar",
         [("Live Topic Search", "Real-time debounced search by academic keyword (e.g. 'OOP', 'Exceptions')."),
          ("Difficulty Filter", "Dropdown filter for All Levels, Easy, Medium, and Hard assessments."),
          ("Age Group Selector", "Dynamic filter for Kids (8-12), Teens (13-17), College (18-22), and Pro (20+).")],
         "Search & Filtering", Inches(4.75), Inches(1.6)),

        ("3. Glassmorphism Quiz Cards Grid",
         [("Multi-Card Layout", "Responsive CSS grid presenting preloaded and instructor-authored assessments."),
          ("Color Badges", "Visual tags for difficulty and colored age badges (pink, cyan, indigo, amber)."),
          ("Action Button", "Displays question count, total marks, and 1-click 'Start Assessment ✍️' trigger.")],
         "Quiz Repository Grid", Inches(8.7), Inches(1.6)),

        # Row 2
        ("4. Active Quiz Runner & Countdown Timer",
         [("10-Minute Timer", "Live countdown ticker in header with automated submission upon time expiry."),
          ("Grading Strategy Switch", "Student selector to attempt quiz under Standard or 25% Negative Marking."),
          ("Polymorphic Inputs", "Renders radio buttons for MCQs, binary toggles for T/F, text fields for Numeric.")],
         "Active Assessment Engine", Inches(0.8), Inches(4.3)),

        ("5. Instant Scorecard Modal & History",
         [("Instant Feedback", "Modal dialog pop-up calculating net marks, percentage, and letter grade (A+, A, B, F)."),
          ("Question Audit", "Color-coded item-by-item breakdown highlighting student choice vs correct answer."),
          ("Submissions Log", "Tabulated history preserving all student attempt timestamps and scores.")],
         "Scorecard & Analytics", Inches(4.75), Inches(4.3)),

        ("6. Faculty Management & CIE-2 Inspector",
         [("Quiz Authoring Modal", "Allows instructors to create custom quizzes and append polymorphic questions."),
          ("Live Viva Inspector", "Dedicated CIE-2 concept defense tab explaining OOP, interfaces, and exceptions."),
          ("1-Click Concept Test", "Button to execute the automated concept verification matrix live in browser.")],
         "Faculty & Concept Defense", Inches(8.7), Inches(4.3))
    ]

    card_w4 = Inches(3.833)
    card_h4 = Inches(2.5)

    for title, items, badge, left_pos, top_pos in ui_components:
        add_card(s4, left_pos, top_pos, card_w4, card_h4, title, items, badge_text=badge, border_color=CARD_BORDER, font_size=8.5)

    # Output file
    out_file = os.path.join(base_dir, "Online_Quiz_Management_System_4Slides.pptx")
    prs.save(out_file)
    print(f"Presentation successfully created and saved at: {out_file}")

if __name__ == "__main__":
    build_4_slide_presentation()
