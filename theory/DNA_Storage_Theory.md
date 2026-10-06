# Theory of DNA Storage & Error Correction

This document summarizes the core theoretical concepts discussed in our term paper on "Error Correction for DNA Storage" by Jin Sima, Netanel Raviv, Moshe Schwartz, and Jehoshua Bruck.

## 1. Why DNA Storage?
Traditional storage media (hard drives, solid-state drives, magnetic tape) are struggling to keep up with the exponential growth of digital data. DNA storage presents an attractive alternative for "cold" storage (seldom accessed archival data) because:
- **Ultra-dense:** A room-sized data center could be compressed into a refrigerator-sized container of DNA.
- **Stability:** Artificial DNA molecules can last tens of thousands of years with zero energy investment (compared to a 20-year lifespan of a hard drive).
- **Future-proof:** As long as humans exist, the technology to read DNA will remain a priority.

## 2. In-vitro vs In-vivo
- **In-vitro:** The DNA sequences are stored in synthetic glass vials. Errors here are mostly deletions and insertions due to synthesis and sequencing defects.
- **In-vivo:** DNA sequences are stored inside living organisms (like bacteria). The self-sustaining property ensures longevity, but introduces a new set of biological "evolutionary" errors, such as duplication during mitosis.

## 3. The Error Types
Unlike traditional media which mostly suffer from **substitutions** (bit-flips, e.g., `1001` -> `1011`), DNA storage is prone to synchronization errors:
- **Deletions:** A nucleotide disappears without a trace (e.g., `TGGA` -> `TGA`).
- **Insertions:** An extra nucleotide appears (e.g., `ACTG` -> `ACCTG`).
- **Duplications:** Sections of DNA are replicated biologically (e.g., Tandem, Interspersed, Reverse-Complement).

## 4. Deletion Codes & Varshamov-Tenengolts (VT)
To correct single deletions, **VT Codes** are used. They work using a weighted modulo summation:
`\sum_{i=1}^{n} i \cdot c_i \equiv 0 \pmod{n+1}`

For multiple deletions, simple weighted sums fail. The breakthrough involves using **Indicator Vectors**, which artificially insert a '0' between every two '1's. This ensures a mathematical structure where higher-order weighted sums can successfully recover multiple missing bits.

## 5. The Sliced Channel
Traditional storage relies on a single continuous string. DNA storage fragments data into multiple unordered short sequences (due to synthesis limits). 
To reassemble the pieces, **indexing** is required. Instead of using redundant bits exclusively for indices, optimal codes use **data-based indexing**, where prefixes represent both data and lexicographical order markers.

## 6. Duplication Cones
In *in-vivo* storage, duplications act as layers of mutations. The set of all possible mutated sequences from an original sequence is called its **Descendant Cone**. Efficient error-correction in living organisms relies on choosing initial DNA sequences such that their descendant cones never overlap.
