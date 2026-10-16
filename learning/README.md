# Learning workspace

## How tutoring works

- Start from your Apache Spark knowledge; spend time on Databricks platform features, workflows, architecture, and the differences that matter in practice.
- Explain a topic clearly, connect it to Spark where useful, then use a small example or exercise when it helps you learn.
- Help with reading comprehension, code, exercises, troubleshooting, quizzes, and review.
- Keep a concise note for each book chapter, section, file, or other reading item you share. Add questions and exercises when useful.
- When notes introduce a concept that applies beyond one book, add it to the combined notes. Add compact recall prompts and key reminders to the revision notes.

## Note workflow

1. Put each reading item's note in that book's `notes/` folder, using an ordered filename where possible, such as `01-chapter-title.md`.
2. Add the note to that book's `README.md` index.
3. Capture reusable concepts in `combined/combined-notes.md` and review prompts in `revision/revision-notes.md`.
4. Keep book-specific claims grounded in material you provide. If a detail is missing, mark it as a question to verify against the book.

## Templates

Use [the reading note template](templates/reading-note-template.md) for chapter and section notes. Adjust it to fit the material rather than filling every heading mechanically.

## First PySpark script

Run `scripts/first_pyspark_script.py` from the repository root in the project environment. It creates a small DataFrame, aggregates completed orders by category, prints the execution plan, and keeps Spark running so you can inspect its UI before pressing Enter to exit.
