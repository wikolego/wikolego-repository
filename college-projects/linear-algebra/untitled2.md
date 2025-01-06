# Zadanie

## Treść

Wyznacz wartości własne i wektory własne oraz sprawdź diagonalizowalność macierzy

$$
\begin{bmatrix}
    1 & 2 & 3 \\
    0 & 4 & 0 \\
    0 & 5 & 6
\end{bmatrix}
$$

## Obliczenia

### Obliczanie wartości własnych

$$
\begin{vmatrix}
    1 - \lambda & 2 & 3 \\
    0 & 4 - \lambda & 0 \\
    0 & 5 & 6 - \lambda
\end{vmatrix}
 = (1 - \lambda) * (4 - \lambda) * (6 - \lambda)
$$

$$
\lambda_1 = 1 \\
\lambda_2 = 4 \\
\lambda_3 = 6
$$

### Obliczanie wektorów własnych

---

Dla lambda = 1

$$
\begin{bmatrix}
    0 & 2 & 3 \\
    0 & 3 & 0 \\
    0 & 5 & 5
\end{bmatrix}

\begin{array}{l}
    \\
    \\
    w_3' = w_3 - w_2 - w_1
\end{array}
$$

$$
\begin{bmatrix}
    0 & 2 & 3 \\
    0 & 3 & 0 \\
    0 & 0 & 2
\end{bmatrix}

\begin{array}{l}
    w_1' =  6 * w_1 \\
    \\
    \\
\end{array}
$$

$$
\begin{bmatrix}
    0 & 12 & 18 \\
    0 & 3 & 0 \\
    0 & 0 & 2
\end{bmatrix}

\begin{array}{l}
    w_1' = w_1 - 4 * w_2 - 9 * w_3 \\
    \\
    \\
\end{array}
$$

---

$$
\begin{array}{}
x_1 & y_1 & z_1
\end{array}
$$

$$
\begin{bmatrix}
    0 & 0 & 0 \\
    0 & 3 & 0 \\
    0 & 0 & 2
\end{bmatrix}
$$

$$
x_1 \in \R \\
y_1 = 0 \\
z_1 = 0
$$

$$
\overrightarrow{v_1}
=
\begin{bmatrix}
    x_1 \\
    0 \\
    0
\end{bmatrix}
=
x_1
\begin{bmatrix}
    1 \\
    0 \\
    0
\end{bmatrix}
$$

---

Dla lambda = 4

$$
\begin{bmatrix}
    -3 & 2 & 3 \\
    0 & 0 & 0 \\
    0 & 5 & 2
\end{bmatrix}

\begin{array}{l}
    \\
    w_2' = w_3 \\
    w_3' = w_2
\end{array}
$$

$$
\begin{bmatrix}
    -3 & 2 & 3 \\
    0 & 5 & 2 \\
    0 & 0 & 0
\end{bmatrix}
$$

---

$$
\begin{array}{}
x_2 & y_2 & z_2
\end{array}
$$

$$
\begin{bmatrix}
    -3 & 2 & 3 \\
    0 & 5 & 2 \\
    0 & 0 & 0
\end{bmatrix}
$$

$$
3x_2 = -\frac{4}{5}z_2 + 3z_2 \\
x_2 = \frac{11}{15}z_2 \\
y_2 = -\frac{2}{5}z_2 \\
z_2 \in \R
$$

$$
\overrightarrow{v_2}
=
\begin{bmatrix}
    \frac{11}{15}z_2 \\
    -\frac{2}{5}z_2 \\
    z_2
\end{bmatrix}
=
z_2
\begin{bmatrix}
    \frac{11}{15} \\
    -\frac{6}{15} \\
    1
\end{bmatrix}
=
\frac{1}{15}z_2
\begin{bmatrix}
    11 \\
    -6 \\
    15
\end{bmatrix}
$$

---

Dla lambda = 6

$$
\begin{bmatrix}
    -5 & 2 & 3 \\
    0 & -2 & 0 \\
    0 & 5 & 0
\end{bmatrix}

\begin{array}{l}
    \\
    w_2' = w_3 + 2*w_2 \\
    w_3' = w_2
\end{array}
$$

$$
\begin{bmatrix}
    -5 & 2 & 3 \\
    0 & 1 & 0 \\
    0 & -2 & 0
\end{bmatrix}

\begin{array}{l}
    \\
    \\
    w_3' = w_3 + 2*w_2
\end{array}
$$

$$
\begin{bmatrix}
    -5 & 2 & 3 \\
    0 & 1 & 0 \\
    0 & 0 & 0
\end{bmatrix}
$$

---

$$
\begin{array}{}
x_3 & y_3 & z_3
\end{array}
$$

$$
\begin{bmatrix}
    -5 & 2 & 3 \\
    0 & 1 & 0 \\
    0 & 0 & 0
\end{bmatrix}
$$

$$
x_3 = \frac{3}{5}z_3 \\
y_3 = 0 \\
z_3 \in \R
$$

$$
\overrightarrow{v_3}
=
\begin{bmatrix}
    \frac{3}{5}z_3 \\
    0 \\
    z_3
\end{bmatrix}
=
z_3
\begin{bmatrix}
    \frac{3}{5} \\
    0 \\
    1
\end{bmatrix}
=
\frac{1}{5}
z_3
\begin{bmatrix}
    3 \\
    0 \\
    5
\end{bmatrix}
$$
