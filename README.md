# Determinant Calculator

A simple Flask web application that computes the determinant of a square matrix using Gaussian elimination.

## Features

- Input an n×n matrix through a web form
- Computes the determinant by row reducing into an upper triangular matrix
- Handles row swaps (with sign correction) and zero-pivot cases
- Built with Flask and NumPy

## Tech Stack

- **Backend:** Python, Flask
- **Math:** NumPy
- **Frontend:** HTML templates (Jinja2), static CSS
- **Deployment:** Procfile included (Heroku-ready)

## Project Structure

```
determinant/
├── app.py              # Flask app + determinant logic
├── templates/          # HTML templates
├── static/             # CSS
├── requirements.txt    # Python dependencies
└── Procfile            # Deployment config
```

## How It Works

The core `det(A)` function in `app.py` works like this:

1. Converts the input matrix to a NumPy float array
2. Iterates through columns and finds a nonzero pivot
3. Swaps rows as needed, tracking the swap count for sign
4. Eliminates entries below each pivot
5. Returns 0 immediately if a column has no nonzero pivot (singular matrix)
6. Multiplies the diagonal of the resulting upper-triangular matrix, applying `(-1)^swaps` for the sign
