
import os

import cv2
import pytesseract


# =========================
# TESSERACT CONFIGURATION
# =========================

WINDOWS_TESSERACT_PATH = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def configure_tesseract() -> None:
    """
    Configure Tesseract for local development.

    Priority:
    1. TESSERACT_CMD environment variable
    2. Default Windows installation path
    3. System PATH
    """

    environment_path = os.getenv("TESSERACT_CMD")

    if environment_path and os.path.isfile(environment_path):
        pytesseract.pytesseract.tesseract_cmd = (
            environment_path
        )
        return

    if (
        os.name == "nt"
        and os.path.isfile(WINDOWS_TESSERACT_PATH)
    ):
        pytesseract.pytesseract.tesseract_cmd = (
            WINDOWS_TESSERACT_PATH
        )


configure_tesseract()


# =========================
# OCR IMAGE PREPROCESSING
# =========================

def prepare_image_for_ocr(image_path: str):
    """
    Prepare a document image before OCR.

    Steps:
    - Validate and load the image
    - Convert to grayscale
    - Upscale small images
    - Reduce noise
    - Apply thresholding to improve text visibility
    """

    if not os.path.isfile(image_path):
        raise FileNotFoundError(
            f"OCR image file does not exist: {image_path}"
        )

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            "Could not read the uploaded image. "
            "Please upload a valid JPG, JPEG, or PNG image."
        )

    grayscale = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )

    height, width = grayscale.shape[:2]

    # Upscale small images to make text easier to recognize.
    if max(width, height) < 1600:
        grayscale = cv2.resize(
            grayscale,
            None,
            fx=2,
            fy=2,
            interpolation=cv2.INTER_CUBIC,
        )

    # Reduce noise without excessively blurring text.
    denoised = cv2.fastNlMeansDenoising(
        grayscale,
        None,
        h=10,
        templateWindowSize=7,
        searchWindowSize=21,
    )

    # Otsu thresholding works well for many scanned documents.
    _, processed_image = cv2.threshold(
        denoised,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )

    return processed_image


# =========================
# EXTRACT TEXT
# =========================

def extract_text_from_image(
    image_path: str,
    language: str = "eng",
) -> str:
    """
    Extract text from a document image using Tesseract OCR.
    """

    processed_image = prepare_image_for_ocr(image_path)

    try:
        extracted_text = pytesseract.image_to_string(
            processed_image,
            lang=language,
            config="--oem 3 --psm 3",
        )

    except pytesseract.TesseractNotFoundError as error:
        raise RuntimeError(
            "Tesseract OCR executable was not found. "
            "Check that Tesseract is installed at "
            f"'{WINDOWS_TESSERACT_PATH}' or set the "
            "TESSERACT_CMD environment variable."
        ) from error

    except pytesseract.TesseractError as error:
        raise RuntimeError(
            f"OCR processing failed: {error}"
        ) from error

    return extracted_text.strip()
