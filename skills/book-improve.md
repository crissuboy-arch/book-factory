# Book Improve Skill

## Description
A specialized skill designed to enhance and refine existing book manuscripts. This skill improves the technical quality, readability, and professional polish of written works while preserving the author's original voice, story, characters, and creative intent. Perfect for self-published authors and those seeking professional editing on a budget.

## Supported Languages
- Portuguese (pt)
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)

## What This Skill Does
- **Orthographic Correction**: Fixes spelling errors, typos, and orthographic mistakes
- **Grammar and Syntax**: Corrects grammatical errors and improves sentence structure
- **Style and Fluency**: Enhances readability and flow without changing meaning
- **Punctuation**: Refines punctuation usage for clarity and professionalism
- **Consistency**: Ensures terminology, character names, and tense consistency throughout
- **Preserves Original Content**: 100% respects the author's story, characters, plot, and creative decisions

## What This Skill Does NOT Do
- Change plot or story structure without explicit author consent
- Alter character motivations or personalities
- Rewrite narrative voice or author's unique style
- Remove or add significant content
- Impose the editor's creative vision over the author's

## Commands

### /improve-book
Analyzes and improves an existing manuscript while maintaining original content integrity.

#### Parameters
- `language`: The language of the book (pt, en, es, fr, de, it)
- `file_input`: The manuscript file (PDF, DOCX, TXT, or markdown)
- `improvement_level`: Basic (spelling/grammar only), Standard (grammar + style), Professional (comprehensive editing)
- `preserve_voice`: Boolean (true to maintain unique author voice, false for standardized tone)
- `focus_areas`: Optional list of specific areas to focus on (e.g., "dialogue,descriptions,pacing")

#### Output Structure
The improved manuscript will include:
1. **Corrected Text**: Full manuscript with all corrections applied
2. **Change Summary**: Detailed list of all modifications made, organized by category
3. **Suggestions Log**: Areas where suggestions were made but not implemented (awaiting author approval)
4. **Style Report**: Analysis of writing style, consistency, and readability enhancements
5. **Quality Metrics**: Before/after scores on grammar, readability, and professionalism
6. **Author Notes**: Recommendations for further improvement (optional)

#### Usage Example
/improve-book language=pt file_input=meu-livro.pdf improvement_level=Professional preserve_voice=true focus_areas="dialogue,descriptions"

## Improvement Levels

### Basic Level
- Spelling corrections
- Basic grammar fixes
- Obvious punctuation errors
- Typo corrections

### Standard Level
- All Basic improvements plus:
- Sentence restructuring for clarity
- Comma splice repairs
- Active vs. passive voice optimization
- Tense consistency
- Repetition reduction

### Professional Level
- All Standard improvements plus:
- Deep style enhancement
- Flow and pacing optimization
- Word choice refinement
- Paragraph coherence
- Consistency across entire manuscript
- Readability enhancement

## Implementation Details

### Correction Categories
1. **Orthography**: Spelling, typos, character encoding issues
2. **Grammar**: Subject-verb agreement, tense, mood, article usage
3. **Punctuation**: Commas, semicolons, dashes, quotation marks
4. **Syntax**: Sentence structure, clause arrangement, clarity
5. **Style**: Repetitive words, passive voice, wordiness, flow
6. **Consistency**: Character names, terminology, formatting, tense

### Voice Preservation Guidelines
- Maintain unique sentence patterns and rhythms
- Keep colloquialisms and dialect if intentional
- Preserve author's narrative perspective
- Respect unique vocabulary choices unless problematic
- Keep emotional tone and pacing intact

### Quality Metrics
- **Readability Score**: 0-100 based on vocabulary, sentence length, complexity
- **Grammar Score**: Percentage of text free from grammatical errors
- **Professionalism Score**: Assessment of polish and publication readiness
- **Consistency Score**: Uniformity of style, terminology, and formatting throughout

## Change Tracking
All changes are documented with:
- Original text → Corrected text
- Reason for change (category)
- Context and line reference
- Author approval required flag (for major changes)

## Acceptance and Revision
- Author can accept, reject, or modify each suggested change
- Detailed explanations for each correction provided
- Alternative suggestions offered when applicable
- Manual review required for subjective improvements

## Ethical Considerations
- Full transparency in all edits
- Respects author's creative vision
- Improves technical quality only
- Clear distinction between necessary and optional improvements
- Author retains full control and final approval

## Limitations
- Cannot significantly restructure plots or rewrite stories
- Not a substitute for developmental editing or content consultation
- May not catch contextual errors or factual inaccuracies
- Subjective style improvements require author approval
- Language-specific nuances may vary by region

## File Format Support
- PDF (with text extraction)
- DOCX (Microsoft Word)
- EPUB (e-books)
- TXT (plain text)
- Markdown (.md)
- ODT (OpenDocument)