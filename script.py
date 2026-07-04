import sys, math, itertools, random, statistics
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QPushButton, QLabel, QLineEdit,
    QDialog, QFormLayout, QMessageBox, QTabWidget, QComboBox,
    QFrame, QScrollArea
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


STYLE = """
QMainWindow, QDialog {
    background-color: #1a1a2e;
}
QGroupBox {
    font: bold 14px 'Segoe UI';
    color: #e0e0e0;
    border: 1px solid #2d2d4e;
    border-radius: 8px;
    margin-top: 14px;
    padding: 16px 12px 12px;
    background-color: #16213e;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 2px 10px;
    background-color: #0f3460;
    border-radius: 4px;
    color: #e94560;
}
QPushButton {
    background-color: #0f3460;
    color: #e0e0e0;
    border: 1px solid #2d2d4e;
    border-radius: 6px;
    padding: 10px 18px;
    font: 13px 'Segoe UI';
    min-height: 20px;
}
QPushButton:hover {
    background-color: #1a4a8a;
    border-color: #e94560;
}
QPushButton:pressed {
    background-color: #0a2647;
}
QPushButton#danger {
    background-color: #a93226;
    border-color: #e74c3c;
}
QPushButton#danger:hover {
    background-color: #c0392b;
}
QPushButton#accent {
    background-color: #e94560;
    border-color: #e94560;
    color: #fff;
    font-weight: bold;
}
QPushButton#accent:hover {
    background-color: #ff6b81;
}
QLineEdit {
    background-color: #0f3460;
    color: #e0e0e0;
    border: 1px solid #2d2d4e;
    border-radius: 6px;
    padding: 8px 12px;
    font: 14px 'Segoe UI';
    selection-background-color: #e94560;
}
QLineEdit:focus {
    border-color: #e94560;
}
QLabel {
    color: #c0c0d0;
    font: 13px 'Segoe UI';
}
QLabel#title {
    font: bold 22px 'Segoe UI';
    color: #e94560;
}
QLabel#result {
    background-color: #0f3460;
    border: 1px solid #2d2d4e;
    border-radius: 6px;
    padding: 10px;
    color: #2ecc71;
    font: 14px 'Segoe UI';
    min-height: 20px;
}
QLabel#subtitle {
    color: #8888aa;
    font: 11px 'Segoe UI';
}
QComboBox {
    background-color: #0f3460;
    color: #e0e0e0;
    border: 1px solid #2d2d4e;
    border-radius: 6px;
    padding: 8px 12px;
    font: 14px 'Segoe UI';
    min-height: 20px;
}
QComboBox:hover {
    border-color: #e94560;
}
QComboBox::drop-down {
    border: none;
    width: 30px;
}
QComboBox QAbstractItemView {
    background-color: #16213e;
    color: #e0e0e0;
    selection-background-color: #e94560;
    border: 1px solid #2d2d4e;
}
QScrollArea { border: none; }
QFrame#card {
    background-color: #16213e;
    border: 1px solid #2d2d4e;
    border-radius: 8px;
    padding: 8px;
}
"""


def float_or_int(x):
    v = float(x)
    return int(v) if v == int(v) else v


def is_num(s):
    s = s.strip()
    if not s:
        return False
    s = s.lstrip('-')
    if not s:
        return False
    parts = s.split('.')
    return len(parts) <= 2 and all(p.isdigit() for p in parts if p)


def is_int(s):
    s = s.strip().lstrip('-')
    return s.isdigit()


class MathDialog(QDialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(400)
        self.setModal(True)
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.title_label = QLabel(title)
        self.title_label.setObjectName("title")
        self.layout.addWidget(self.title_label)
        self.form = QFormLayout()
        self.form.setSpacing(10)
        self.form.setLabelAlignment(Qt.AlignRight)
        self.layout.addLayout(self.form)
        self.result_label = QLabel("")
        self.result_label.setObjectName("result")
        self.result_label.setWordWrap(True)
        self.layout.addWidget(self.result_label)
        self.inputs = []

    def add_input(self, label, placeholder=""):
        inp = QLineEdit()
        inp.setPlaceholderText(placeholder)
        self.form.addRow(QLabel(label), inp)
        self.inputs.append(inp)
        return inp

    def add_combo(self, label, items):
        cb = QComboBox()
        cb.addItems(items)
        self.form.addRow(QLabel(label), cb)
        self.inputs.append(cb)
        return cb

    def get_vals(self):
        return [i.text().strip() for i in self.inputs if isinstance(i, QLineEdit)]

    def show_result(self, text, ok=True):
        color = "#2ecc71" if ok else "#e74c3c"
        self.result_label.setStyleSheet(f"color: {color}; background-color: #0f3460; border: 1px solid #2d2d4e; border-radius: 6px; padding: 10px; font: 14px 'Segoe UI'; min-height: 20px;")
        self.result_label.setText(text)

    def add_button(self, text, callback, accent=True):
        btn = QPushButton(text)
        btn.setObjectName("accent" if accent else "")
        btn.clicked.connect(callback)
        self.layout.addWidget(btn)
        return btn

    def add_close(self):
        btn = QPushButton("Close")
        btn.setObjectName("danger")
        btn.clicked.connect(self.close)
        self.layout.addWidget(btn)


class SqrtDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Square Root")
        self.add_input("Number:", "e.g. 25")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        if not is_num(v):
            return self.show_result("Enter valid number.", False)
        n = float(v)
        if n < 0:
            return self.show_result("Cannot sqrt negative number.", False)
        r = math.sqrt(n)
        self.show_result(f"√{float_or_int(n)} = {r:.6f}")


class PowerDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Power")
        self.add_input("Base:", "e.g. 2")
        self.add_input("Exponent:", "e.g. 10")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        a, b = self.get_vals()
        if not is_num(a) or not is_num(b):
            return self.show_result("Enter valid numbers.", False)
        base, exp = float(a), float(b)
        r = base ** exp
        self.show_result(f"{float_or_int(base)} ^ {float_or_int(exp)} = {r:.6f}")


class PrimeDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Prime Checker")
        self.add_input("Number:", "positive integer")
        self.add_button("Check", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        if not v.isdigit():
            return self.show_result("Enter positive integer.", False)
        n = int(v)
        if n < 2:
            return self.show_result(f"{n} is NOT prime.", False)
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return self.show_result(f"{n} is NOT prime. Divisible by {i}.", False)
        self.show_result(f"{n} is PRIME.")


class PrimeFactorDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Prime Factorization")
        self.add_input("Number:", "positive integer > 1")
        self.add_button("Factorize", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        if not v.isdigit() or int(v) < 2:
            return self.show_result("Enter integer > 1.", False)
        n = int(v)
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1 if d == 2 else 2
        if n > 1:
            factors.append(n)
        from collections import Counter
        cnt = Counter(factors)
        parts = [f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(cnt.items())]
        self.show_result(" × ".join(parts))


class PolygonDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Polygon Interior Angle")
        self.add_input("Number of sides:", "e.g. 6")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        if not v.isdigit() or int(v) < 3:
            return self.show_result("Enter integer ≥ 3.", False)
        n = int(v)
        angle = (n - 2) * 180 / n
        total = (n - 2) * 180
        self.show_result(f"Total interior: {total}°\nEach angle: {angle:.2f}°")


class CircleDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Circle Calculator")
        self.add_input("Radius:", "e.g. 5")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        if not is_num(v) or float(v) <= 0:
            return self.show_result("Enter positive radius.", False)
        r = float(v)
        area = math.pi * r ** 2
        circ = 2 * math.pi * r
        self.show_result(f"Radius = {r}\nArea = {area:.4f}\nCircumference = {circ:.4f}")


class PythagorasDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Pythagoras Theorem")
        self.add_input("Side A:", "e.g. 3")
        self.add_input("Side B:", "e.g. 4")
        self.add_button("Calculate Hypotenuse", self.calc)
        self.add_close()

    def calc(self):
        a, b = self.get_vals()
        if not is_num(a) or not is_num(b):
            return self.show_result("Enter valid numbers.", False)
        x, y = float(a), float(b)
        if x <= 0 or y <= 0:
            return self.show_result("Sides must be positive.", False)
        c = math.hypot(x, y)
        self.show_result(f"A = {x}, B = {y}\nHypotenuse C = {c:.4f}")


class PercentageDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Percentage Calculator")
        self.add_input("Total:", "e.g. 200")
        self.add_input("Percent:", "e.g. 15")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        t, p = self.get_vals()
        if not is_num(t) or not is_num(p):
            return self.show_result("Enter valid numbers.", False)
        total, percent = float(t), float(p)
        r = total * percent / 100
        self.show_result(f"{percent}% of {float_or_int(total)} = {r:.4f}")


class GcdLcmDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("GCD & LCM")
        self.add_input("Number 1:", "e.g. 12")
        self.add_input("Number 2:", "e.g. 18")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        a, b = self.get_vals()
        if not a.isdigit() or not b.isdigit():
            return self.show_result("Enter positive integers.", False)
        x, y = int(a), int(b)
        g = math.gcd(x, y)
        l = x * y // g
        self.show_result(f"GCD({x}, {y}) = {g}\nLCM({x}, {y}) = {l}")


class TrigDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Trigonometry")
        self.mode_cb = self.add_combo("Mode:", ["Degrees", "Radians"])
        self.add_input("Angle:", "e.g. 45")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        if not is_num(v):
            return self.show_result("Enter valid number.", False)
        angle = float(v)
        mode = self.mode_cb.currentText()
        rad = math.radians(angle) if mode == "Degrees" else angle
        sin_v = math.sin(rad)
        cos_v = math.cos(rad)
        tan_v = math.tan(rad) if abs(cos_v) > 1e-12 else "undefined"
        deg_str = f" ({angle}°)" if mode == "Degrees" else ""
        lines = [
            f"sin({angle}) = {sin_v:.6f}",
            f"cos({angle}) = {cos_v:.6f}",
            f"tan({angle}) = {tan_v:.6f}" if isinstance(tan_v, str) else f"tan({angle}) = {tan_v:.6f}",
            "",
            f"sin⁻¹ → {math.degrees(math.asin(sin_v)):.2f}°" if mode == "Degrees" else f"asin → {math.asin(sin_v):.4f} rad",
            f"cos⁻¹ → {math.degrees(math.acos(cos_v)):.2f}°" if mode == "Degrees" else f"acos → {math.acos(cos_v):.4f} rad",
        ]
        self.show_result("\n".join(lines))


class LogDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Logarithms")
        self.add_input("Number:", "e.g. 100")
        self.add_input("Base (optional):", "leave empty for base 10")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        vals = self.get_vals()
        if not is_num(vals[0]):
            return self.show_result("Enter valid number.", False)
        n = float(vals[0])
        if n <= 0:
            return self.show_result("Number must be positive.", False)
        ln = math.log(n)
        log10 = math.log10(n)
        lines = [f"ln({float_or_int(n)}) = {ln:.6f}", f"log₁₀({float_or_int(n)}) = {log10:.6f}"]
        if vals[1] and is_num(vals[1]):
            b = float(vals[1])
            if b <= 0 or b == 1:
                return self.show_result("Base must be > 0 and ≠ 1.", False)
            logb = math.log(n, b)
            lines.append(f"log_{float_or_int(b)}({float_or_int(n)}) = {logb:.6f}")
        self.show_result("\n".join(lines))


class FactorialDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Factorial")
        self.add_input("Number:", "non-negative integer")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        if not v.isdigit():
            return self.show_result("Enter non-negative integer.", False)
        n = int(v)
        if n > 500:
            return self.show_result("Number too large (max 500).", False)
        r = math.factorial(n)
        r_str = f"{r}" if len(str(r)) < 60 else f"{r:.6e}"
        self.show_result(f"{n}! = {r_str}")


class CombinatoricsDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Combinations & Permutations")
        self.add_input("n (total):", "e.g. 10")
        self.add_input("r (choose):", "e.g. 3")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        a, b = self.get_vals()
        if not a.isdigit() or not b.isdigit():
            return self.show_result("Enter positive integers.", False)
        n, r = int(a), int(b)
        if r > n:
            return self.show_result("r cannot exceed n.", False)
        c = math.comb(n, r)
        p = math.perm(n, r)
        self.show_result(f"C({n}, {r}) = {c:,}\nP({n}, {r}) = {p:,}")


class QuadraticDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Quadratic Solver")
        self.add_input("Coefficient a:", "ax² + bx + c = 0")
        self.add_input("Coefficient b:", "")
        self.add_input("Coefficient c:", "")
        self.add_button("Solve", self.calc)
        self.add_close()

    def calc(self):
        a, b, c = self.get_vals()
        if not all(is_num(x) for x in (a, b, c)):
            return self.show_result("Enter valid numbers.", False)
        A, B, C = float(a), float(b), float(c)
        if A == 0:
            if B == 0:
                return self.show_result("No solution (a and b both zero).", False)
            return self.show_result(f"Linear: x = {-C/B:.4f}")
        disc = B ** 2 - 4 * A * C
        if disc > 0:
            x1 = (-B + math.sqrt(disc)) / (2 * A)
            x2 = (-B - math.sqrt(disc)) / (2 * A)
            self.show_result(f"x₁ = {x1:.4f}\nx₂ = {x2:.4f}\nDiscriminant Δ = {disc:.4f}")
        elif disc == 0:
            x = -B / (2 * A)
            self.show_result(f"Double root: x = {x:.4f}\nΔ = 0")
        else:
            real = -B / (2 * A)
            imag = math.sqrt(-disc) / (2 * A)
            self.show_result(f"x₁ = {real:.4f} + {imag:.4f}i\nx₂ = {real:.4f} - {imag:.4f}i\nΔ = {disc:.4f}")


class StatsDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Statistics")
        self.add_input("Numbers (comma separated):", "e.g. 3, 7, 2, 9, 4")
        self.add_button("Calculate", self.calc)
        self.add_close()

    def calc(self):
        v = self.get_vals()[0]
        parts = [x.strip() for x in v.split(",") if x.strip()]
        if len(parts) < 2:
            return self.show_result("Enter at least 2 numbers.", False)
        nums = []
        for p in parts:
            if not is_num(p):
                return self.show_result(f"Invalid number: {p}", False)
            nums.append(float(p))
        mu = statistics.mean(nums)
        med = statistics.median(nums)
        try:
            mode = statistics.mode(nums)
        except statistics.StatisticsError:
            mode = "multiple"
        stdev = statistics.stdev(nums) if len(nums) > 1 else 0
        var = statistics.variance(nums) if len(nums) > 1 else 0
        self.show_result(
            f"Count: {len(nums)}\nMean: {mu:.4f}\nMedian: {med:.4f}\n"
            f"Mode: {mode}\nStd Dev: {stdev:.4f}\nVariance: {var:.4f}"
        )


class BaseConverterDialog(MathDialog):
    def __init__(self, parent=None):
        super().__init__("Number Base Converter")
        self.from_cb = self.add_combo("From base:", ["2 (Binary)", "8 (Octal)", "10 (Decimal)", "16 (Hex)"])
        self.to_cb = self.add_combo("To base:", ["2 (Binary)", "8 (Octal)", "10 (Decimal)", "16 (Hex)"])
        self.add_input("Value:", "e.g. FF")
        self.add_button("Convert", self.calc)
        self.add_close()
        self.base_map = {"2 (Binary)": 2, "8 (Octal)": 8, "10 (Decimal)": 10, "16 (Hex)": 16}

    def calc(self):
        v = self.get_vals()[0]
        if not v.strip():
            return self.show_result("Enter a value.", False)
        from_b = self.base_map[self.from_cb.currentText()]
        to_b = self.base_map[self.to_cb.currentText()]
        try:
            n = int(v.strip(), from_b)
            prefixes = {2: "0b", 8: "0o", 10: "", 16: "0x"}
            if to_b == 10:
                result = str(n)
            else:
                result = format(n, ["b", "o", "d", "x"][[2, 8, 10, 16].index(to_b)])
            self.show_result(f"{v.strip()} (base {from_b}) = {result} (base {to_b})")
        except ValueError:
            self.show_result(f"Invalid value for base {from_b}.", False)


class CalculatorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculator")
        self.setMinimumWidth(380)
        self.setModal(True)
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 16, 16, 16)
        title = QLabel("Calculator")
        title.setObjectName("title")
        layout.addWidget(title)
        self.display = QLineEdit()
        self.display.setPlaceholderText("0")
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet(
            "background-color: #0f3460; color: #e0e0e0; border: 1px solid #2d2d4e; "
            "border-radius: 6px; padding: 12px; font: 22px 'Segoe UI'; min-height: 30px;"
        )
        layout.addWidget(self.display)
        self.result = QLabel("")
        self.result.setObjectName("result")
        layout.addWidget(self.result)
        grid = QGridLayout()
        grid.setSpacing(6)
        btns = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("C", 3, 2), ("+", 3, 3),
        ]
        for text, r, c in btns:
            btn = QPushButton(text)
            btn.setMinimumHeight(50)
            if text in "+-*/":
                btn.setObjectName("accent")
            elif text == "C":
                btn.setObjectName("danger")
            else:
                btn.setStyleSheet(
                    "QPushButton { background-color: #1a1a2e; color: #e0e0e0; border: 1px solid #2d2d4e; "
                    "border-radius: 6px; font: 16px 'Segoe UI'; }"
                    "QPushButton:hover { background-color: #0f3460; border-color: #e94560; }"
                )
            btn.clicked.connect(lambda checked, t=text: self.on_btn(t))
            grid.addWidget(btn, r, c)
        eq_btn = QPushButton("=")
        eq_btn.setObjectName("accent")
        eq_btn.setMinimumHeight(50)
        eq_btn.clicked.connect(self.calc)
        grid.addWidget(eq_btn, 4, 0, 1, 4)
        layout.addLayout(grid)
        close_btn = QPushButton("Close")
        close_btn.setObjectName("danger")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

    def on_btn(self, t):
        if t == "C":
            self.display.clear()
            self.result.clear()
            return
        current = self.display.text()
        if t in "+-*/":
            if current and current[-1] not in "+-*/":
                self.display.setText(current + t)
        else:
            if current == "0" and t != ".":
                self.display.setText(t)
            else:
                self.display.setText(current + t)

    def calc(self):
        expr = self.display.text().strip()
        allowed = set("0123456789.+-*/() ")
        if not expr:
            return
        if any(c not in allowed for c in expr):
            self.result.setText("Error: invalid chars")
            self.result.setStyleSheet("color: #e74c3c; background-color: #0f3460; border: 1px solid #2d2d4e; border-radius: 6px; padding: 10px;")
            return
        try:
            r = eval(expr)
            self.result.setText(f"= {r:.6f}".rstrip("0").rstrip("."))
            self.result.setStyleSheet("color: #2ecc71; background-color: #0f3460; border: 1px solid #2d2d4e; border-radius: 6px; padding: 10px;")
        except Exception:
            self.result.setText("Error: invalid expression")
            self.result.setStyleSheet("color: #e74c3c; background-color: #0f3460; border: 1px solid #2d2d4e; border-radius: 6px; padding: 10px;")


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        self.setFixedSize(420, 200)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        title = QLabel("Smart Math")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        info = QLabel(
            "Developer: Seyyed Shayan Seyyedi\n"
            "Language: Python + PyQt5\n"
            "Purpose: Multi-purpose mathematical calculator\n"
            "Features: Algebra, Geometry, Trigonometry,\n"
            "          Statistics, Number Theory & more"
        )
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("color: #c0c0d0; font: 13px 'Segoe UI'; line-height: 1.6;")
        layout.addWidget(info)
        btn = QPushButton("Close")
        btn.setObjectName("danger")
        btn.clicked.connect(self.close)
        layout.addWidget(btn)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Math")
        self.setMinimumSize(700, 520)
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        header = QLabel("Smart Math")
        header.setObjectName("title")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        sub = QLabel("Multi-purpose mathematical toolbox")
        sub.setObjectName("subtitle")
        sub.setAlignment(Qt.AlignCenter)
        layout.addWidget(sub)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        scroll_w = QWidget()
        scroll_w.setStyleSheet("background-color: transparent;")
        gl = QGridLayout(scroll_w)
        gl.setSpacing(12)

        modules = [
            ("Algebra", [
                ("Calculator", CalculatorDialog),
                ("Power", PowerDialog),
                ("Square Root", SqrtDialog),
                ("Quadratic Solver", QuadraticDialog),
            ]),
            ("Number Theory", [
                ("Prime Checker", PrimeDialog),
                ("Prime Factors", PrimeFactorDialog),
                ("GCD & LCM", GcdLcmDialog),
                ("Factorial", FactorialDialog),
            ]),
            ("Geometry", [
                ("Circle", CircleDialog),
                ("Polygon Angle", PolygonDialog),
                ("Pythagoras", PythagorasDialog),
            ]),
            ("Trig & Log", [
                ("Trigonometry", TrigDialog),
                ("Logarithms", LogDialog),
            ]),
            ("Combinatorics", [
                ("Combinations / Perms", CombinatoricsDialog),
            ]),
            ("Statistics & Conversion", [
                ("Statistics", StatsDialog),
                ("Base Converter", BaseConverterDialog),
                ("Percentage", PercentageDialog),
            ]),
        ]

        row, col = 0, 0
        for title, items in modules:
            group = QGroupBox(title)
            vbox = QVBoxLayout(group)
            vbox.setSpacing(6)
            for label, dlg_cls in items:
                def make_handler(c):
                    return lambda: c(self).exec_()
                btn = QPushButton(label)
                btn.clicked.connect(make_handler(dlg_cls))
                vbox.addWidget(btn)
            gl.addWidget(group, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        scroll.setWidget(scroll_w)
        layout.addWidget(scroll, 1)

        footer = QHBoxLayout()
        footer.setSpacing(10)
        gh_btn = QPushButton("GitHub")
        gh_btn.setObjectName("accent")
        gh_btn.clicked.connect(lambda: __import__("webbrowser").open("https://github.com/ShayanCoder710/"))
        footer.addWidget(gh_btn)
        about_btn = QPushButton("About")
        about_btn.clicked.connect(lambda: AboutDialog(self).exec_())
        about_btn.setStyleSheet(
            "QPushButton { background-color: #0f3460; color: #e0e0e0; border: 1px solid #2d2d4e; "
            "border-radius: 6px; padding: 10px 18px; font: 13px 'Segoe UI'; }"
            "QPushButton:hover { background-color: #1a4a8a; border-color: #e94560; }"
        )
        footer.addWidget(about_btn)
        exit_btn = QPushButton("Exit")
        exit_btn.setObjectName("danger")
        exit_btn.clicked.connect(self.close)
        footer.addWidget(exit_btn)
        layout.addLayout(footer)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
