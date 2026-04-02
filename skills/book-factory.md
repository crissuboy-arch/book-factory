# Book Factory Skill

## Description
A comprehensive skill for generating complete book manuscripts in multiple languages and genres. This skill leverages AI to create fictional or non-fictional content based on user-specified parameters.

## Supported Languages
- Portuguese (pt)
- English (en)
- Spanish (es)
- French (fr)

## Supported Genres
- Romance
- Thriller
- Fantasy
- Self-help
- Short Stories (Contos)

## Commands

### /book-create
Generates a complete book manuscript including title, characters, chapters, and synopsis.

#### Parameters
- `language`: The language of the book (pt, en, es, fr)
- `theme`: The central theme or topic of the book (e.g., "love in the city", "mysterious murder", "magical adventure")
- `genre`: The genre of the book (romance, thriller, fantasy, self-help, short-stories)
- `type`: The type of content (full-book for complete novels, short-story for concise narratives)
- `chapters`: Number of chapters for full-book (10, 20, 30, or 60; ignored for short-story)

#### Output Structure
The generated manuscript will include:
1. **Title**: An engaging title in the specified language
2. **Subtitle**: A complementary subtitle enhancing the title
3. **Cover Synopsis**: A compelling blurb for the book cover (150-250 words)
4. **Author Biography**: A fictional or generated author bio (100-200 words)
5. **Characters**: A list of main characters with brief descriptions
6. **Synopsis**: A detailed summary of the plot
7. **Table of Contents/Index**: Complete list of chapters with page numbers (estimated)
8. **Chapters**: For full-book: The specified number of complete chapters (10, 20, 30, or 60), each with at least 2000 words; for short-story: A single complete narrative
9. **Chapter Image Descriptions**: Detailed descriptions for AI-generated images or illustrations for each chapter
10. **Quality Score**: A rating out of 10 based on originality, coherence, engagement, and adherence to genre conventions
11. **Formatted Files**: Ready-to-upload files formatted for Amazon KDP (EPUB/DOCX) and Hotmart (PDF/EPUB)

#### Usage Example
/book-create language=en theme="a forbidden love story in Victorian England" genre=romance type=full-book chapters=20

## Implementation Details

### Genre-Specific Guidelines
- **Romance**: Focus on emotional connections, conflicts, and happy endings
- **Thriller**: Build suspense, include twists, mystery elements
- **Fantasy**: Incorporate magical elements, world-building, mythical creatures
- **Self-help**: Provide practical advice, motivational content, step-by-step guidance
- **Short Stories**: Concise narratives with clear beginning, middle, and end

### Language Adaptation
- Ensure all generated content is in the specified language
- Use appropriate cultural references and idioms for each language
- Maintain grammatical correctness and natural flow

### Content Quality Standards
- Original, creative content
- Age-appropriate (general audience)
- Respectful and inclusive
- Avoid harmful stereotypes or offensive material

### Generation Process
1. Analyze the theme, genre, and chapter count to determine plot structure and pacing
2. Create compelling characters that fit the theme
3. Develop a coherent storyline with appropriate pacing across the specified number of chapters
4. Generate detailed cover elements: title, subtitle, cover synopsis, author biography
5. Create a complete table of contents with estimated page numbers
6. Write full chapters, each with at least 2000 words, ensuring narrative progression
7. Generate detailed image descriptions for each chapter to aid in visual representation
8. Format the entire manuscript for publication on Amazon KDP and Hotmart
9. Ensure the synopsis captures the essence of the story

### Quality Scoring System
After generating the manuscript, evaluate it on a scale of 1-10 across the following criteria:
- **Originality (1-10)**: How unique and creative the content is
- **Coherence (1-10)**: Logical flow of plot and character development
- **Engagement (1-10)**: Ability to captivate the reader
- **Genre Adherence (1-10)**: How well it fits the chosen genre conventions
- **Overall Score**: Average of the above, with justification for the rating

Provide feedback on strengths and areas for improvement.

## Publication Formatting Instructions

### General Formatting for All Platforms
- **Font and Spacing**: Use 12pt Times New Roman or Garamond for body text, 14pt for chapter titles, 1.5 line spacing, 1-inch margins on all sides.
- **Page Breaks**: Insert page breaks before each chapter, table of contents, and back matter.
- **Headers/Footers**: Include page numbers in footer, book title and author name in header (except first page).
- **Front Matter**: Title page, copyright page, dedication, table of contents, foreword (if applicable).
- **Back Matter**: Author biography, acknowledgments, about the author, other books by author.
- **Images**: Placeholder text for image descriptions; actual images to be generated separately using AI tools like DALL-E or Midjourney based on provided descriptions.
- **Word Count**: Ensure each chapter meets minimum 2000 words; total book should align with chosen chapter count (e.g., 20 chapters x 2000 words = ~40,000 words minimum).
- **Proofreading**: Run spell check and grammar check in the target language.

### Amazon KDP (Kindle Direct Publishing)
- **File Format**: Export as DOCX for upload, or convert to EPUB using Calibre. Ensure no embedded fonts unless necessary.
- **Cover**: Use the generated cover text elements; design cover with title, subtitle, author name prominently. Dimensions: 2560 x 1600 pixels for full cover.
- **Metadata**: Use cover synopsis as description, add 7 keywords, select BISAC categories matching genre.
- **Pricing**: Base on word count (e.g., 40,000 words ~ $4.99), enroll in KDP Select for wider distribution.
- **Upload Process**: Upload manuscript and cover separately, preview with Kindle Previewer, publish.

### Hotmart
- **File Format**: Export as PDF (print-ready) or EPUB. Embed fonts, ensure high-resolution images.
- **Cover and Description**: Use generated cover synopsis and biography; create eye-catching cover design.
- **Product Page**: Title with subtitle, detailed description using synopsis, author bio in "About the Author" section.
- **Pricing and Sales**: Set price, enable one-time purchase or subscription, set up affiliate commissions.
- **Delivery**: Host files on Hotmart or use external links; provide download instructions.
- **Marketing Tools**: Create bundles, upsells, email sequences, and promotional pages.

Ensure compliance with each platform's content guidelines, including no offensive material and proper copyright notices.
- If an unsupported language is provided, default to English and notify the user
- If the theme is too vague, ask for clarification
- Handle generation failures gracefully with alternative suggestions

## Limitations
- Generated content is for entertainment and inspiration purposes only
- Not intended for commercial use without proper editing and review
- AI-generated content may require human refinement for publication quality