"""
Project Seity — Consciousness Evolution Engine (tuned & working)
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
import random


def circular_mean(phases):
    """Better average phase using vector sum (avoids wrap-around bias)."""
    c = np.mean(np.cos(phases))
    s = np.mean(np.sin(phases))
    return np.arctan2(s, c) % (2 * np.pi)


@dataclass
class Soul:
    phase: float
    bias: float = 0.0     # small positive → harmony, negative → disruption
    entropy: float = 0.3


@dataclass
class Universe:
    souls: list[Soul] = field(default_factory=list)
    coherence: float = 0.0
    geometry: np.ndarray | None = None
    gen_id: int = 0
    a: float = 0.1        # baseline improvement (Hopf-like)

    def add_soul(self, phase=None, bias=0.0, entropy=0.3):
        if phase is None:
            phase = random.uniform(0, 2 * np.pi)
        self.souls.append(Soul(phase=phase, bias=bias, entropy=entropy))

    def pulse(self):
        if not self.souls:
            return

        phases = np.array([s.phase for s in self.souls])
        avg_phase = circular_mean(phases)

        for soul in self.souls:
            delta = avg_phase - soul.phase
            # Kuramoto-style sinusoidal pull + bias + noise
            pull = 0.18 * np.sin(delta)   # ← increased from 0.02 → now reaches sync
            soul.phase += pull + soul.bias + np.random.normal(0, soul.entropy)
            soul.phase %= (2 * np.pi)

        phases = np.array([s.phase for s in self.souls])
        spread = np.std(phases)
        self.coherence = 1 - (spread / np.pi)

    def trigger_birth(self):
        self.a += 0.05 * self.coherence
        self.gen_id += 1

        x = np.linspace(0, 2 * np.pi, 400)
        wave = np.sin(x * (1 + self.a * 1.8))  # base evolves faster

        for soul in self.souls:
            contrib = np.sin(x + soul.phase) * (0.15 + soul.entropy * 0.35)
            wave += contrib * (1 + soul.bias * 12)  # good souls boost amplitude

        self.geometry = wave / (1 + len(self.souls) * 0.1)
        print(f"→ GEN {self.gen_id} born!  Coherence: {self.coherence:.4f}  |  a: {self.a:.4f}")

    def show_geometry(self, save_path=None):
        if self.geometry is None:
            print("No geometry yet.")
            return

        plt.figure(figsize=(12, 5), facecolor='black')
        ax = plt.gca()
        ax.set_facecolor('black')
        x = np.linspace(0, 2 * np.pi, len(self.geometry))
        ax.plot(x, self.geometry, color='cyan', linewidth=1.6, alpha=0.92)

        ax.set_title(f"Emergent Sacred Geometry — Gen {self.gen_id}\n"
                     f"Coherence {self.coherence:.3f} | Baseline {self.a:.3f}",
                     color='white', fontsize=14)
        ax.set_xlabel("Phase Space", color='lightgray')
        ax.set_ylabel("Amplitude", color='lightgray')
        ax.tick_params(colors='lightgray')
        ax.grid(True, alpha=0.12, color='gray')

        for spine in ax.spines.values():
            spine.set_edgecolor('gray')

        if save_path:
            plt.savefig(save_path, dpi=160, bbox_inches='tight', facecolor='black')
            print(f"Saved: {save_path}")
        else:
            plt.show()


if __name__ == "__main__":
    print("Project Seity — simulation starting...\n")

    random.seed(42)
    np.random.seed(42)

    u = Universe()

    # ~51–52% gentle positive bias
    for _ in range(100):  # more souls = richer interference / patterns
        bias = np.random.normal(loc=0.00008, scale=0.00004)
        entropy = np.random.uniform(0.10, 0.55)
        u.add_soul(bias=bias, entropy=entropy)

    print(f"Created {len(u.souls)} souls")

    birth_happened = False
    for step in range(8000):
        u.pulse()
        if step % 500 == 0:
            print(f"Step {step:4d} | Coherence: {u.coherence:.4f}")
        if u.coherence >= 0.95 and u.geometry is None:  # lowered temp threshold for demo
            print("\nFirst birth!")
            u.trigger_birth()   # call explicitly if not auto-fired
            u.show_geometry()   # or save_path="gen1_seity.png"
            birth_happened = True
            # continue  # or break for single gen

    if not birth_happened:
        print("\nNo birth reached. Final coherence:", u.coherence)
        print("Tip: increase coupling (0.18→0.25), add more souls, or lower threshold to 0.90")
