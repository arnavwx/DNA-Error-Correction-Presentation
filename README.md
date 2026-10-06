# Error Correction for DNA Storage (InC Infojatt)

Welcome to the Infocom Term Paper Presentation repository for **Error Correction for DNA Storage**! This repository documents our research, presentation materials, and theoretical breakdowns based on the paper by Jin Sima, Netanel Raviv, Moshe Schwartz, and Jehoshua Bruck. 

## Repository Structure

- **[`Team_8_Error_Correction_for_DNA_Storage.pdf`](./Team_8_Error_Correction_for_DNA_Storage.pdf)**: The primary research paper assigned to our group.
- **[`Final_Presentation.mp4`](./Final_Presentation.mp4)**: The final compiled presentation video showcasing our work.
- **[`manim/`](./manim)**: Contains the `dna_presentation.py` script, which houses the complete source code used to generate the 13 mathematical animations and slides for the presentation.
- **[`theory/`](./theory)**: Contains [`DNA_Storage_Theory.md`](./theory/DNA_Storage_Theory.md), a comprehensive summary of the core concepts, error channels, and coding mechanisms described in the paper.
- **[`references/`](./references)**: Contains [`References_List.md`](./references/References_List.md), an organized list of the academic papers and foundational theories referenced throughout this project.

## Running the Manim Code

To reproduce the animated slides locally, you need to have Python and [Manim](https://docs.manim.community/en/stable/installation.html) installed on your machine.

1. Navigate to the `manim` directory:
   ```bash
   cd manim
   ```
2. Run the command to generate a specific scene (for example, the title slide):
   ```bash
   manim -pqh dna_presentation.py Slide01_Title
   ```
   *Replace `Slide01_Title` with the name of the desired scene. (Available scenes: `Slide01_Title`, `Slide02_WhyDNA`, `Slide03_HowDNA`, `Slide04_ErrorTypes`, `Slide05_ErrorBalls`, `Slide06_VTCodes`, `Slide07_MultipleDeletions`, `Slide08_SlicedChannel`, `Slide09_Indexing`, `Slide10_Duplication`, `Slide11a_DuplicationCones`, `Slide11b_DuplicationDecoding`, `Slide12_Summary`)*

## Key Concepts Explored
- **In-vitro & In-vivo Storage**: Using glass vials versus living organisms for data longevity.
- **Synchronization Errors**: Handling deletions, insertions, and biological duplications (Tandem, Interspersed, Reverse-Complement).
- **Varshamov-Tenengolts (VT) Codes**: Mathematical models (weighted modulo summations) to correct deleted bits.
- **Sliced Channel Indexing**: Solving order-loss in unordered DNA strands without heavy redundant indexing bits.

---
**Team:** InC Infojatt  
*For educational and archival purposes.*
