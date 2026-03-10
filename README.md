<<<<<<< HEAD
# stylometric-plagiarism-detector

A command-line tool that detects which author, among a set of texts, is most likely infected by COH-PIAH — a fictional linguistic disease from an introductory MIT/MIT-inspired programming course. The detection is based on comparing stylometric signatures extracted from each text.

---

## Overview

COH-PIAH affects writing style in measurable ways. This program computes a **linguistic signature** for each input text and compares it against a known infected signature, returning the text most likely written by the infected author.

| Feature | Description |
|--------|-------------|
| Language | Python 3 |
| Input | Manual (terminal) |
| Output | Index of the most likely infected text |

---

## Linguistic Signature

Each text is analyzed across six stylometric traits:

| Trait | Description |
|-------|-------------|
| WAL — Average Word Length | Mean number of characters per word |
| TTR — Type-Token Ratio | Ratio of unique words to total words |
| HLR — Hapax Legomena Ratio | Ratio of words that appear only once to total words |
| SAL — Average Sentence Length | Mean number of characters per sentence |
| SAC — Average Sentence Complexity | Mean number of phrases per sentence |
| PAL — Average Phrase Length | Mean number of characters per phrase |

Similarity between two signatures is calculated as the mean absolute difference across all six traits. The lower the score, the closer the match.

---

## Project Structure

```
stylometric-plagiarism-detector/
├── detector.py   # Full implementation
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/stylometric-plagiarism-detector.git
cd stylometric-plagiarism-detector
```

### 2. Run the program

```bash
python detector.py
```

No external dependencies — uses only Python's built-in `re` module.

---

## Usage

The program runs interactively in the terminal and follows two steps.

**Step 1 — Enter the known infected signature:**
```
Entre o tamanho médio de palavra: 4.3
Entre a relação Type-Token: 0.7
Entre a Razão Hapax Legomana: 0.5
Entre o tamanho médio de sentença: 80.2
Entre a complexidade média da sentença: 2.1
Entre o tamanho medio de frase: 38.4
```

**Step 2 — Enter the texts to be compared (press Enter on an empty line to finish):**
```
Digite o texto 1 (aperte enter para sair): Lorem ipsum...
Digite o texto 2 (aperte enter para sair): Dolor sit amet...
Digite o texto 3 (aperte enter para sair):
```

**Output:**
```
O autor do texto 2 está infectado com COH-PIAH
```

---

## How It Works

1. The program reads the known infected signature (6 float values)
2. For each input text, it extracts sentences, phrases, and words using regex
3. It computes the six stylometric traits for each text
4. It compares each text's signature against the infected signature using mean absolute difference
5. It returns the index of the text with the lowest difference score

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
=======
# USP-Project

Small codes, developed in the programming course at the University of São Paulo. Each code has a different purpose.
>>>>>>> 0062c653d56e925499dbf7165b0b35eeeaeb8d55
