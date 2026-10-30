import os
import zipfile
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table, TableStyle, Spacer, KeepInFrame

NAME = "Hamidur Khan"
STUDENT_ID = "002475552"
TEST_ACC = "0.963"
MEAN_ACC = "0.973"
STD_ACC = "0.020"

HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(HERE, "screenshots")
PDF = os.path.join(HERE, "Naive_Bayes_Report.pdf")
ZIP = os.path.join(HERE, "Naive_Bayes_Submission.zip")

pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", "C:/Windows/Fonts/ariali.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic")

missing = [f for f in ["fig1_venv.png", "fig2_results.png", "fig3_histogram.png"]
           if not os.path.isfile(os.path.join(SHOTS, f))]
if missing:
    raise SystemExit(f"Missing screenshots in {SHOTS}:\n  " + "\n  ".join(missing))

styles = getSampleStyleSheet()
title = ParagraphStyle("t", parent=styles["Title"], fontName="Arial-Bold", fontSize=14, spaceAfter=2)
sub = ParagraphStyle("s", parent=styles["Normal"], fontName="Arial", fontSize=12, alignment=1, spaceAfter=4)
h = ParagraphStyle("h", parent=styles["Heading3"], fontName="Arial-Bold", fontSize=11, spaceBefore=6, spaceAfter=2)
body = ParagraphStyle("b", parent=styles["Normal"], fontName="Arial", fontSize=12, leading=12)
cap = ParagraphStyle("c", parent=styles["Italic"], fontName="Arial-Italic", fontSize=12, alignment=1)


def fig(name, max_w, max_h):
    path = os.path.join(SHOTS, name)
    w, h_ = ImageReader(path).getSize()
    s = min(max_w / w, max_h / h_)
    return Image(path, w * s, h_ * s)


page_w = A4[0] - 3 * cm
col_w = (page_w - 0.4 * cm) / 2

story = [
    Paragraph("Exercise: Naive Bayes Classification of Wine Data", title),
    # Paragraph(f"{NAME} &middot; {STUDENT_ID} &middot; {date.today():%d.%m.%Y}", sub),

    Paragraph("1. Environment", h),
    Paragraph(
        "A Python virtual environment was created with <font face='Courier'>python -m venv .venv</font>, "
        "activated, and the required packages (numpy, pandas, matplotlib, scikit-learn, ipykernel) were installed "
        "into it. The notebook was executed with the <font face='Courier'>.venv</font> kernel.", body),
    Spacer(1, 3),
    # fig("fig1_venv.png", page_w, 5 * cm),
    # Paragraph("Fig. 1. Virtual environment activated and packages installed.", cap),

    Paragraph("2. Data and method", h),
    Paragraph(
        "The UCI Wine dataset contains 178 wines from three cultivars, each described by 13 chemical features. "
        "The exploratory plots in the notebook show that features such as Flavanoids, and Proline "
        "separate the classes well, but the correlation matrix also shows that many features are correlated, "
        "which violates the independence assumption of Naive Bayes. The data was split randomly into 70 % training "
        "and 30 % test data. A <b>GaussianNB</b> classifier from scikit-learn was trained: it estimates the class "
        "priors P(y) and, for every class and feature, a Gaussian mean and "
        "variance, then predicts the class. ", body),

    Paragraph("3. Results", h),
    Paragraph(
        f"On the test set the classifier reached an accuracy of <b>{TEST_ACC}</b>; the confusion matrix and "
        "per-class precision/recall are shown in Fig. 1. Because a single random split is noisy, the split and "
        f"training were repeated 100 times, giving a mean test accuracy of <b>{MEAN_ACC} &plusmn; {STD_ACC}</b> (Fig. 2).", body),
    Spacer(1, 3),
]

figs = Table(
    [[fig("fig2_results.png", col_w, 10 * cm), fig("fig3_histogram.png", col_w, 10 * cm)],
     [Paragraph("Fig. 1. Accuracy, confusion matrix and classification report.", cap),
      Paragraph("Fig. 2. Test accuracy over 100 random train/test splits.", cap)]],
    colWidths=[col_w + 0.2 * cm] * 2,
)
figs.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                          ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
story += [figs,
          Paragraph("4. Conclusion", h),
          Paragraph(
              "Even though the features are not independent, Gaussian Naive Bayes classifies the wine cultivars "
              "very accurately (about 97 % on average) with almost no tuning and very fast training. The few errors "
              "occur between cultivars whose feature distributions overlap, mostly involving class 2.", body)]

doc = SimpleDocTemplate(PDF, pagesize=A4, leftMargin=1.5 * cm, rightMargin=1.5 * cm,
                        topMargin=1.2 * cm, bottomMargin=1.2 * cm)
doc.build([KeepInFrame(doc.width, doc.height, story, mode="shrink")])

with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for f in ["Naive_Bayes_Report.pdf", "Naive_Bayes_Classification.ipynb", "wine.data.csv"]:
        z.write(os.path.join(HERE, f), f)

print("Wrote", PDF)
print("Wrote", ZIP)
