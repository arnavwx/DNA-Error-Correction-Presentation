from manim import *

class Slide01_Title(Scene):
    def construct(self):
        title = Text("Error Correction for DNA Storage", font_size=48, color=BLUE)
        authors = Text("Jin Sima, Netanel Raviv, Moshe Schwartz, Jehoshua Bruck", font_size=24)
        subtitle = Text("Presented by InC Infojatt", font_size=32, color=YELLOW)
        
        VGroup(title, authors, subtitle).arrange(DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(authors))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(2)

class Slide02_WhyDNA(Scene):
    def construct(self):
        title = Text("Why DNA Storage?", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))

        pt1 = Text("• Ultra-dense: Refrigerator-sized data centers", font_size=30)
        pt2 = Text("• Stable: Lasts tens of thousands of years", font_size=30)
        pt3 = Text("• Future-proof: DNA reading technology will always exist", font_size=30)
        
        pts = VGroup(pt1, pt2, pt3).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        pts.next_to(title, DOWN, buff=1)
        
        for pt in pts:
            self.play(FadeIn(pt, shift=RIGHT))
            self.wait(1)
            
        self.wait(2)

class Slide03_HowDNA(Scene):
    def construct(self):
        title = Text("DNA Storage Workflow", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        steps = [
            "Data (0s and 1s)",
            "Encode (A, C, G, T)",
            "Synthesize & Store",
            "Amplify (PCR)",
            "Sequence (Read)",
            "Decode to Data"
        ]
        
        boxes = VGroup(*[Text(s, font_size=24) for s in steps]).arrange(DOWN, buff=0.4)
        
        arrows = VGroup(*[Arrow(UP, DOWN, buff=0.1).scale(0.5) for _ in range(len(steps)-1)])
        
        workflow = VGroup()
        for i in range(len(steps)):
            workflow.add(boxes[i])
            if i < len(steps) - 1:
                arrows[i].next_to(boxes[i], DOWN, buff=0.1)
                boxes[i+1].next_to(arrows[i], DOWN, buff=0.1)
                workflow.add(arrows[i])
                
        workflow.move_to(ORIGIN)
        
        for item in workflow:
            self.play(FadeIn(item, shift=UP))
            self.wait(0.5)
            
        self.wait(2)

class Slide04_ErrorTypes(Scene):
    def construct(self):
        title = Text("Types of Errors", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        sub_title = Text("Substitution", font_size=32, color=YELLOW)
        sub_ex = Text("TGGA → TGGG", font_size=28)
        
        del_title = Text("Deletion", font_size=32, color=RED)
        del_ex = Text("TGGA → TGA", font_size=28)
        
        ins_title = Text("Insertion", font_size=32, color=GREEN)
        ins_ex = Text("ACTG → ACCTG", font_size=28)
        
        v1 = VGroup(sub_title, sub_ex).arrange(DOWN)
        v2 = VGroup(del_title, del_ex).arrange(DOWN)
        v3 = VGroup(ins_title, ins_ex).arrange(DOWN)
        
        all_errors = VGroup(v1, v2, v3).arrange(RIGHT, buff=1).center()
        
        self.play(FadeIn(v1))
        self.wait(1)
        self.play(FadeIn(v2))
        self.wait(1)
        self.play(FadeIn(v3))
        self.wait(2)

class Slide05_ErrorBalls(Scene):
    def construct(self):
        title = Text("Error Balls: Substitution vs Deletion", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        sub_desc = Text("Substitution Ball (Input: 1001, 1 error):", font_size=24)
        sub_set = Text("{1001, 0001, 1101, 1011, 1000}", font_size=24, color=YELLOW)
        VGroup(sub_desc, sub_set).arrange(DOWN).shift(UP*1)
        
        del_desc = Text("Deletion Ball (Input: 1001, 1 error):", font_size=24)
        del_set = Text("{1001, 001, 101, 100}", font_size=24, color=RED) # Note: paper uses 1001, actually deletion from 1001 gives 001, 101, 100.
        VGroup(del_desc, del_set).arrange(DOWN).shift(DOWN*1)
        
        self.play(Write(sub_desc), FadeIn(sub_set))
        self.wait(2)
        self.play(Write(del_desc), FadeIn(del_set))
        self.wait(2)

class Slide06_VTCodes(Scene):
    def construct(self):
        title = Text("Varshamov-Tenengolts (VT) Codes", font_size=40, color=BLUE).to_edge(UP)
        
        desc = Text("Corrects a single deletion using modulo summation:", font_size=28)
        formula = MathTex(r"\sum_{i=1}^{n} i \cdot c_i \equiv 0 \pmod{n+1}")
        
        ex_desc = Text("Example: Sequence 00110 (missing 1 bit)", font_size=28)
        ex_ans = Text("Correct sequence is 001100 (sum = 3+4=7 ≡ 0 mod 7)", font_size=28, color=GREEN)
        
        content = VGroup(desc, formula, ex_desc, ex_ans).arrange(DOWN, buff=0.7)
        
        self.play(Write(title))
        self.play(FadeIn(desc), Write(formula))
        self.wait(2)
        self.play(FadeIn(ex_desc))
        self.wait(1)
        self.play(FadeIn(ex_ans))
        self.wait(2)

class Slide07_MultipleDeletions(Scene):
    def construct(self):
        title = Text("Multiple Deletions", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        pt1 = Text("Weighted modulo sums aren't enough for multiple deletions.", font_size=28)
        pt2 = Text("Indicator Vectors: Introduce '0's between '1's.", font_size=28)
        pt3 = Text("With indicator vectors, higher-order sums can correct multiple errors.", font_size=28, color=YELLOW)
        
        pts = VGroup(pt1, pt2, pt3).arrange(DOWN, buff=0.7)
        
        for pt in pts:
            self.play(FadeIn(pt, shift=LEFT))
            self.wait(2)

class Slide08_SlicedChannel(Scene):
    def construct(self):
        title = Text("The Sliced Channel", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        trad = Text("Traditional: Single long sequence", font_size=30, color=RED)
        dna = Text("DNA Storage: Multiple short, unordered sequences", font_size=30, color=GREEN)
        
        VGroup(trad, dna).arrange(DOWN, buff=0.5).shift(UP*1)
        
        self.play(Write(trad))
        self.play(Write(dna))
        self.wait(2)
        
        problem = Text("Problem: Loss of sequence order (Indexing needed)", font_size=28, color=YELLOW).shift(DOWN*1)
        self.play(FadeIn(problem))
        self.wait(2)

class Slide09_Indexing(Scene):
    def construct(self):
        title = Text("Indexing & Sliced Codes", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        sol1 = Text("1. Standard Indexing: Dedicate bits to store the index.", font_size=28)
        sol2 = Text("2. Data-based Indexing: Use data itself for indexing.", font_size=28, color=GREEN)
        
        desc = Text("Prefixes in sequences act as both data and order markers (lexicographic).", font_size=24).next_to(sol2, DOWN)
        
        self.play(FadeIn(sol1))
        self.wait(2)
        self.play(FadeIn(sol2))
        self.play(Write(desc))
        self.wait(3)

class Slide10_Duplication(Scene):
    def construct(self):
        title = Text("In-vivo Storage: Duplication Errors", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        types = VGroup(
            Text("• Tandem: ACCTAGGA → ACCTACTAGGA", font_size=28),
            Text("• Interspersed: ACCTAGGA → ACCTAGGCTAA", font_size=28),
            Text("• Reverse-Complement: ACCTAGGA → ACCTATAGGGA", font_size=28),
            Text("• End Duplication: ACCTAGGA → ACCTAGGACTA", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(FadeIn(types, lag_ratio=0.5))
        self.wait(3)

class Slide11a_DuplicationCones(Scene):
    def construct(self):
        title = Text("Descendant Cones & Capacity", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        cone_txt = Text("Descendant Cone: Set of all possible mutated outcomes.", font_size=28)
        cap_txt = Text("Capacity: The exponential growth rate of the cone.", font_size=28)
        
        VGroup(cone_txt, cap_txt).arrange(DOWN, buff=0.5).center()
        
        self.play(Write(cone_txt))
        self.wait(1)
        self.play(Write(cap_txt))
        self.wait(2)

class Slide11b_DuplicationDecoding(Scene):
    def construct(self):
        title = Text("De-duplication & Roots", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        dedup = Text("De-duplication: Undoing the duplication mutations.", font_size=28)
        root = Text("Root: The base sequence after all de-duplications.", font_size=28)
        
        ex = Text("Example: 210121010 → 21010 → 210", font_size=28, color=YELLOW)
        
        VGroup(dedup, root, ex).arrange(DOWN, buff=0.7)
        
        self.play(FadeIn(dedup))
        self.play(FadeIn(root))
        self.wait(1)
        self.play(Write(ex))
        self.wait(2)

class Slide12_Summary(Scene):
    def construct(self):
        title = Text("Summary", font_size=40, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        pts = VGroup(
            Text("1. DNA is an ultra-dense, stable medium for cold storage.", font_size=28),
            Text("2. Suffers from deletion, insertion, and substitution errors.", font_size=28),
            Text("3. VT Codes & Indicator Vectors correct these errors.", font_size=28),
            Text("4. Sliced channels require efficient indexing schemes.", font_size=28),
            Text("5. In-vivo storage introduces duplication errors.", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        for pt in pts:
            self.play(FadeIn(pt, shift=RIGHT))
            self.wait(1)
            
        self.wait(3)
