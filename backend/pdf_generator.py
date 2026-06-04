from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(result):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    # --------------------------
    # Title
    # --------------------------

    content.append(
        Paragraph(
            "AI Interview Evaluation Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    # --------------------------
    # Candidate Details
    # --------------------------

    content.append(
        Paragraph(
            f"<b>Candidate:</b> {result['username']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Final Score:</b> {result['score']}/100",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    # --------------------------
    # Question
    # --------------------------

    content.append(
        Paragraph(
            "<b>Interview Question</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["question"],
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    # --------------------------
    # Candidate Answer
    # --------------------------

    content.append(
        Paragraph(
            "<b>Candidate Answer</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            result["candidate_answer"],
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    # --------------------------
    # NLP Metrics
    # --------------------------

    content.append(
        Paragraph(
            "<b>NLP Evaluation Breakdown</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Semantic Similarity: {result['semantic']:.2f}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Keyword Coverage: {result['keyword']:.2f}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Completeness: {result['completeness']:.2f}%",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    # --------------------------
    # Strengths
    # --------------------------

    content.append(
        Paragraph(
            "<b>Strengths</b>",
            styles["Heading2"]
        )
    )

    for item in result["strengths"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    # --------------------------
    # Weaknesses
    # --------------------------

    content.append(
        Paragraph(
            "<b>Weaknesses</b>",
            styles["Heading2"]
        )
    )

    for item in result["weaknesses"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    # --------------------------
    # Suggestions
    # --------------------------

    content.append(
        Paragraph(
            "<b>Suggestions</b>",
            styles["Heading2"]
        )
    )

    for item in result["suggestions"]:
        content.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    content.append(PageBreak())

    # --------------------------
    # Ideal Answer
    # --------------------------

    content.append(
        Paragraph(
            "<b>Ideal Answer</b>",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            result["ideal_answer"],
            styles["Normal"]
        )
    )

    doc.build(content)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf