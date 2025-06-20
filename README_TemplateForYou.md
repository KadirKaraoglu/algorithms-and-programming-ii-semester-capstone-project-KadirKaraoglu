# [The Boyer-Moore Algorithm] - Interactive Visualization

## Project Overview

This project is an interactive web application that implements and visualizes [Algorithm Name], developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

The Boyer-Moore algorithm improves performance by skipping sections of the text using information from the pattern.
It achieves this through two preprocessing heuristics:

- Bad Character Heuristic

- Good Suffix Heuristic

Main Idea
The pattern is aligned with the beginning of the text.
Characters are compared right to left.
If a mismatch is found, the algorithm shifts the pattern by a smart amount instead of just one character.
This reduces unnecessary comparisons and leads to faster execution, especially for long texts and complex patterns.

The Boyer-Moore algorithm is particularly effective when the alphabet is moderately sized and the pattern is relatively short compared to the text.

### Problem Definition

The string search problem involves finding all occurrences of a substring (called the pattern) within a larger string (called the text). This is a fundamental problem in computer science with applications in search engines, bioinformatics, text processing, and more.

### Mathematical Background

The Boyer-Moore algorithm uses two heuristics to improve search efficiency:

- Bad Character Heuristic: When a mismatch occurs, the pattern is shifted so the mismatched character in the text aligns with the last occurrence of that character in the pattern.

- ood Suffix Heuristic: When a suffix of the pattern matches the text but is followed by a mismatch, the algorithm shifts the pattern to align the next occurrence of this suffix (if any) or a prefix that matches a suffix.

### Algorithm Steps


1. Preprocessing Phase:

- Compute the Bad Character Table.

- Compute the Good Suffix Shift Table.

2. Searching Phase:

Start aligning the pattern at the beginning of the text.
Compare characters from right to left.

On mismatch:

- Apply the maximum of the bad character and good suffix shifts.

On complete match:

- Record the position.
- Shift pattern based on good suffix table.

### Pseudocode

Function BoyerMooreSearch(text, pattern):
    Preprocess pattern to build bad character table
    Preprocess pattern to build good suffix table
    Set s = 0  // current shift of pattern over text

    While s <= length(text) - length(pattern):
        Set j = last index of pattern

        While j >= 0 and pattern[j] == text[s + j]:
            j = j - 1

        If j < 0:
            Record match at position s
            s = s + good_suffix[0]
        Else:
            shift_bad = j - last_occurrence[text[s + j]]
            shift_good = good_suffix[j + 1]
            s = s + max(shift_bad, shift_good)


## Complexity Analysis

### Time Complexity

- Best Case: O(n/m) — when mismatches happen early and frequently.
- Average Case: O(n) — linear performance in practice with good heuristics.
- Worst Case: O(n * m) — rare, when heuristics fail due to repeated patterns.

### Space Complexity

O(m + σ)

- m: length of the pattern
- σ: size of the alphabet (for bad character table)

## Features

- Clean Streamlit interface
- Boyer-Moore algorithm search
- Bad character and good suffix heuristics
- Highlights found patterns in the text
- Supports multiple matches
- Responsive and fast visualization

## Screenshots

![Main Interface](docs/screenshots/main_interface.png)
*Caption describing the main interface*

![Algorithm in Action](docs/screenshots/algorithm_demo.png)
*Caption describing the algorithm in action*

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Enter the text to search in the "Text" field.
2. Enter the pattern you want to search for.
3. Click the Search button.
4. The app highlights all occurrences of the pattern in yellow.
5. The indices where the pattern is found are listed below.

### Example Inputs

1.   Text: abacaabaccabacabaabb
     Pattern: abacab
     Output: Found at index 10

2.   Text: THIS IS A TEST TEXT
     Pattern: TEST
     Output: Found at index 10

3.   Text: AABAACAADAABAABA
     Pattern: AABA
     Output: Found at indices 0, 9, 12

## Implementation Details

### Key Components

- algorithm.py: Contains the core Boyer-Moore search algorithm and both heuristics.
- app.py: Streamlit app where user interacts with the algorithm.
- visualizer.py: Handles the visualization of search results in the UI.

### Code Highlights

```python
def visualize_search_results(text, pattern, indices):
    # Highlights all found patterns in the text
    for start_idx in indices:
        end_idx = start_idx + len(pattern)
        highlighted_text += f"<span style='background-color: yellow;'>{text[start_idx:end_idx]}</span>"
```

## Testing

This project includes a test suite to verify the correctness of the algorithm implementation:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

- Basic Search Tests
   Tests simple cases where the pattern appears exactly once in the text.
   Example: Searching "ABC" in "ABAAABCD" returns index [4].
   Ensures the algorithm correctly finds a single occurrence.

- Multiple Occurrences Tests
   Checks if the algorithm can detect multiple, possibly overlapping occurrences of the pattern within the text.
   Example: Searching "VUR" in "DAVULCU VUR DAVULAAAA VUR VUR DURMA" returns [8, 22, 26].
   Also tests repetitive characters like "AA" in "AAAAA" returning all valid matches.

- No Occurrence Tests
   Verifies that the algorithm returns an empty list when the pattern does not appear in the text at all.
   Example: Searching "KADIR" in "Hello World" returns [].

- Empty Pattern Tests
   Ensures that an empty pattern is considered to match at every possible position in the text, including the empty text.
   Example: Searching "" in "abc" returns [0, 1, 2, 3].

- Empty Text Tests
   Confirms that searching any non-empty pattern in an empty text returns no matches.
   Example: Searching "abc" in "" returns [].

- Pattern Longer Than Text Tests
   Ensures that when the pattern length exceeds the text length, no matches are found.
   Example: Searching "longer pattern than text" in "short" returns [].

- Single Character Pattern Tests
   Tests patterns consisting of a single character, verifying all its occurrences are found.
   Example: Searching "A" in "KADIR KARAOGLU" returns [1, 7, 9].

## Live Demo

A live demo of this application is available at: [Insert Streamlit Cloud URL here]

## Limitations and Future Improvements

### Current Limitations

- Only supports plain-text (no regex or case-insensitive matching)
- No step-by-step visualization (only final result)

### Planned Improvements

- Add character-by-character animation of the search
- Support for regex-like matching
- Dark mode and better UI theme

## References and Resources

### Academic References

1. [Reference 1]
2. [Reference 2]
3. [Reference 3]

### Online Resources

- [\[Resource 1\]](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm)
- [\[Resource 3\]](https://gemini.google.com)

## Author

- **Name:** [Kadir Karaoğlu]
- **Student ID:** [230543005 ]
- **GitHub:** [KadirKaraoglu]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project, and [any other acknowledgements].

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
