import math
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Tuple

@dataclass
class HistoryItem:
    action: str
    detail: str
    timestamp: str

class HistoryManager:
    def __init__(self) -> None:
        self._items: List[HistoryItem] = []

    def add(self, action: str, detail: str) -> None:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._items.append(HistoryItem(action, detail, ts))

    def items(self) -> List[HistoryItem]:
        return list(self._items)

    def print(self) -> None:
        if not self._items:
            print("Chưa có phép tính nào được thực hiện.")
            return
        print("---- LỊCH SỬ PHÉP TÍNH ----")
        for i, it in enumerate(self._items, start=1):
            print(f"{i}. [{it.timestamp}] {it.action} → {it.detail}")

class MathCalculator:
    def __init__(self, history: Optional[HistoryManager] = None) -> None:
        self.history = history or HistoryManager()

    def basic_ops(self, a: float, b: float) -> Tuple[float, float, float, Optional[float]]:
        tong = a + b
        hieu = a - b
        tich = a * b
        thuong = None if b == 0 else a / b
        detail = f"a={a}, b={b} → +={tong}, -={hieu}, *={tich}, /={'Không chia 0' if thuong is None else thuong}"
        self.history.add("Cơ bản (+ - * /)", detail)
        return tong, hieu, tich, thuong

    def power(self, a: float, b: float) -> float:
        kq = a ** b
        self.history.add("Lũy thừa", f"{a}^{b} = {kq}")
        return kq

    def sqrt_pair(self, a: float, b: float) -> Tuple[Optional[float], Optional[float]]:
        def safe_sqrt(x: float) -> Optional[float]:
            return math.sqrt(x) if x >= 0 else None
        sa = safe_sqrt(a)
        sb = safe_sqrt(b)
        da = f"√{a}={'Lỗi: số âm' if sa is None else sa}"
        db = f"√{b}={'Lỗi: số âm' if sb is None else sb}"
        self.history.add("Căn bậc hai", f"{da}, {db}")
        return sa, sb

    def trig_deg(self, a_deg: float, b_deg: float) -> dict:
        a = math.radians(a_deg)
        b = math.radians(b_deg)
        out = {
            f"sin({a_deg}°)": math.sin(a),
            f"cos({a_deg}°)": math.cos(a),
            f"tan({a_deg}°)": math.tan(a),
            f"sin({b_deg}°)": math.sin(b),
            f"cos({b_deg}°)": math.cos(b),
            f"tan({b_deg}°)": math.tan(b),
        }
        self.history.add("Hàm lượng giác", f"a={a_deg}°, b={b_deg}° → {out}")
        return out

    def log_ops(self, a: float, base: Optional[float] = None) -> dict:
        if a <= 0:
            self.history.add("Logarit", f"a={a} (Lỗi: a phải > 0)")
            raise ValueError("a phải > 0 để tính log.")
        result = {"log10(a)": math.log10(a), "ln(a)": math.log(a)}
        if base is not None:
            if base > 0 and base != 1:
                result[f"log_{base}(a)"] = math.log(a, base)
            else:
                result["base_error"] = "Cơ số không hợp lệ (base > 0 và base != 1)."
        self.history.add("Logarit", f"a={a}, base={base} → {result}")
        return result

    def solve_linear(self, a: float, b: float) -> float:
        if a == 0:
            self.history.add("PT bậc nhất", f"a={a}, b={b} (Lỗi: a phải ≠ 0)")
            raise ValueError("Hệ số 'a' phải khác 0.")
        x = -b / a
        self.history.add("PT bậc nhất", f"{a}x + {b} = 0 → x = {x}")
        return x

    def solve_quadratic(self, a: float, b: float, c: float) -> Tuple[str, Tuple[Optional[float], Optional[float]]]:
        if a == 0:
            self.history.add("PT bậc hai", f"a={a} (Lỗi: a phải ≠ 0)")
            raise ValueError("Hệ số 'a' phải khác 0.")
        delta = b**2 - 4*a*c
        if delta < 0:
            self.history.add("PT bậc hai", f"a={a}, b={b}, c={c} → vô nghiệm (Δ={delta})")
            return "Vô nghiệm", (None, None)
        elif delta == 0:
            x = -b / (2*a)
            self.history.add("PT bậc hai", f"a={a}, b={b}, c={c} → nghiệm kép x={x} (Δ=0)")
            return "Nghiệm kép", (x, x)
        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-b + sqrt_delta) / (2*a)
            x2 = (-b - sqrt_delta) / (2*a)
            self.history.add("PT bậc hai", f"a={a}, b={b}, c={c} → x1={x1}, x2={x2} (Δ={delta})")
            return "Hai nghiệm phân biệt", (x1, x2)

    def current_time(self) -> str:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.add("Xem thời gian", now)
        return now
