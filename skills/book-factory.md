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

#### Output Structure
The generated manuscript will include:
1. **Title**: An engaging title in the specified language
2. **Characters**: A list of main characters with brief descriptions
3. **Synopsis**: A summary of the plot
4. **Chapters**: Outline of chapter titles and brief descriptions (for full books) or complete short stories

#### Usage Example
/book-create language=en theme="a forbidden love story in Victorian England"

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
1. Analyze the theme and genre to determine plot structure
2. Create compelling characters that fit the theme
3. Develop a coherent storyline with appropriate pacing
4. Generate chapter outlines or full content based on genre
5. Ensure the synopsis captures the essence of the story

## Error Handling
- If an unsupported language is provided, default to English and notify the user
- If the theme is too vague, ask for clarification
- Handle generation failures gracefully with alternative suggestions

## Limitations
- Generated content is for entertainment and inspiration purposes only
- Not intended for commercial use without proper editing and review
- AI-generated content may require human refinement for publication quality