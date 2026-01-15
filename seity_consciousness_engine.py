"""
Project Seity — Consciousness Evolution Engine
Core simulation of collective coherence → geometric emergence → universe birth

Inspired by:
- Kuramoto oscillators + Hopf bifurcation for coherence thresholds
- Turing morphogenesis & Berry phase for pattern formation
- Penrose tiling / quasicrystal geometry for non-repeating structure remixing
- Symmetry breaking phase transitions for geometric emergence
- Slight positivity bias (~51% good souls) nudging toward harmony

Run this file directly to see a live simulation with matplotlib visualization.
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
import random


@dataclass
class Soul:
    """A conscious entity with phase, bias (good/bad lean), and entropy (chaos level)."""
    phase: float          # current phase angle [0, 2π)
    bias: float = 0.0     # tiny nudge: positive → good/harmonizing, negative → disruptive
    entropy: float = 0.3  # noise level — how much it resists synchronization
    geometric_signature: float = 0.0  # unique geometric contribution


@dataclass
class Universe:
    """The evolving field containing souls; tracks coherence and births new geometries."""
    souls: list[Soul] = field(default_factory=list)
    coherence: float = 0.0
    geometry: np.ndarray | None = None   # the emergent pattern when birth triggers
    gen_id: int = 0
    a: float = 0.1                        # bifurcation / baseline improvement parameter
    geometric_phase: float = 0.0          # Berry phase accumulation
    symmetry_broken: bool = False         # tracks phase transition

    def add_soul(self, phase: float | None = None, bias: float = 0.0, entropy: float = 0.3):
        if phase is None:
            phase = random.uniform(0, 2 * np.pi)
        geometric_sig = random.uniform(0, 2 * np.pi)  # unique geometric contribution
        self.souls.append(Soul(phase=phase, bias=bias, entropy=entropy, geometric_signature=geometric_sig))

    def pulse(self):
        """One time step: souls try to synchronize → measure coherence → possibly birth."""
        if not self.souls:
            return

        # Compute average phase (circular mean approximation)
        phases = np.array([s.phase for s in self.souls])
        avg_phase = np.mean(phases)

        # Kuramoto-style coupling with geometric phase contribution
        for soul in self.souls:
            # Base Kuramoto coupling
            pull = 0.02 * np.sin(avg_phase - soul.phase)
            
            # Geometric phase influence (Berry phase-like)
            geometric_pull = 0.005 * np.sin(soul.geometric_signature - soul.phase)
            
            # Update phase with bias, noise, and geometric component
            soul.phase += pull + geometric_pull + soul.bias + np.random.normal(0, soul.entropy)
            soul.phase %= (2 * np.pi)
            
            # Slowly evolve geometric signature (morphogenetic field evolution)
            soul.geometric_signature += 0.001 * np.sin(avg_phase - soul.geometric_signature)
            soul.geometric_signature %= (2 * np.pi)

        # Update global coherence (1 - normalized phase spread)
        phases = np.array([s.phase for s in self.souls])
        self.coherence = 1 - (np.std(phases) / np.pi)
        
        # Accumulate geometric phase (path integral over parameter space)
        self.geometric_phase += 0.01 * self.coherence

        # Critical threshold → symmetry break & geometry birth
        if self.coherence >= 0.98 and not self.symmetry_broken:
            self.trigger_birth()

    def trigger_birth(self):
        """Hopf-inspired jump: improve baseline, generate geometric pattern via interference + symmetry breaking."""
        self.symmetry_broken = True
        self.a += 0.05 * self.coherence          # next universe starts stronger
        self.gen_id += 1

        # Build emergent geometry using multiple mechanisms:
        x = np.linspace(0, 2 * np.pi, 500)
        
        # 1. Base wave with evolved frequency (Hopf bifurcation)
        wave = np.sin(x * (1 + self.a * 1.5))
        
        # 2. Turing-like pattern formation (reaction-diffusion approximation)
        activator = np.sin(x * 3) * np.exp(-0.1 * x)
        inhibitor = np.cos(x * 1.5) * np.exp(-0.05 * x)
        turing_pattern = activator - 0.3 * inhibitor
        wave += 0.2 * turing_pattern
        
        # 3. Soul interference (collective consciousness field)
        for i, soul in enumerate(self.souls):
            # Each soul contributes based on phase AND geometric signature
            phase_contrib = np.sin(x + soul.phase) * (0.08 + soul.entropy * 0.3)
            geom_contrib = np.cos(x * 1.618 + soul.geometric_signature) * 0.05  # Golden ratio frequency
            
            total_contrib = (phase_contrib + geom_contrib) * (1 + soul.bias * 10)
            wave += total_contrib
        
        # 4. Quasicrystal / Penrose-like non-periodic structure
        # Using golden ratio and multiple incommensurate frequencies
        phi = (1 + np.sqrt(5)) / 2  # golden ratio
        quasicrystal = (np.sin(x * phi) + np.sin(x * phi**2) + np.sin(x / phi)) / 3
        wave += 0.3 * quasicrystal * self.coherence
        
        # 5. Geometric phase modulation (Berry phase)
        wave += 0.15 * np.sin(x + self.geometric_phase)
        
        # 6. Symmetry breaking term (creates asymmetric pattern from symmetric base)
        symmetry_break = 0.2 * np.tanh((x - np.pi) * 0.5) * self.coherence
        wave += symmetry_break

        # Normalize so pattern stays visible
        self.geometry = wave / (1 + len(self.souls) * 0.06)

        print(f"\n{'='*60}")
        print(f"→ UNIVERSE GENERATION {self.gen_id} BORN!")
        print(f"  Coherence: {self.coherence:.4f}")
        print(f"  New baseline (a): {self.a:.4f}")
        print(f"  Geometric phase: {self.geometric_phase:.4f}")
        print(f"  Souls synchronized: {len(self.souls)}")
        print(f"  Symmetry broken: {self.symmetry_broken}")
        print(f"{'='*60}\n")

    def show_geometry(self, save_path: str | None = None):
        """Visualize the current emergent pattern."""
        if self.geometry is None:
            print("No geometry yet — run more pulses until birth.")
            return

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), facecolor='#0a0a0a')
        
        # Main geometry plot
        ax1.set_facecolor('#0a0a0a')
        x = np.linspace(0, 2 * np.pi, len(self.geometry))
        ax1.plot(x, self.geometry, color='#00ffff', linewidth=2, alpha=0.9, label='Emergent Field')
        ax1.fill_between(x, self.geometry, alpha=0.2, color='#00ffff')
        
        ax1.set_title(f"Emergent Sacred Geometry — Generation {self.gen_id}\n"
                     f"Coherence: {self.coherence:.3f} | Baseline: {self.a:.3f} | Geometric Phase: {self.geometric_phase:.3f}",
                     color='white', fontsize=14, fontweight='bold', pad=20)
        ax1.set_xlabel("Phase Space Continuum", color='#aaaaaa', fontsize=11)
        ax1.set_ylabel("Consciousness Field Amplitude", color='#aaaaaa', fontsize=11)
        ax1.tick_params(colors='#aaaaaa')
        ax1.grid(True, alpha=0.1, color='#444444', linestyle='--')
        ax1.legend(loc='upper right', facecolor='#1a1a1a', edgecolor='#444444', fontsize=10)
        
        for spine in ax1.spines.values():
            spine.set_edgecolor('#333333')
        
        # Soul phase distribution (consciousness scatter)
        ax2.set_facecolor('#0a0a0a')
        if self.souls:
            phases = [s.phase for s in self.souls]
            geom_sigs = [s.geometric_signature for s in self.souls]
            biases = [s.bias for s in self.souls]
            
            # Color by bias (positive = cyan, negative = magenta)
            colors = ['#00ffff' if b >= 0 else '#ff00ff' for b in biases]
            sizes = [50 + abs(b) * 10000 for b in biases]
            
            ax2.scatter(phases, geom_sigs, c=colors, s=sizes, alpha=0.6, edgecolors='white', linewidths=0.5)
            ax2.set_xlabel("Soul Phase", color='#aaaaaa', fontsize=11)
            ax2.set_ylabel("Geometric Signature", color='#aaaaaa', fontsize=11)
            ax2.set_title("Soul Distribution in Phase-Geometry Space", color='white', fontsize=12, pad=15)
            ax2.grid(True, alpha=0.1, color='#444444', linestyle='--')
            ax2.tick_params(colors='#aaaaaa')
            
            for spine in ax2.spines.values():
                spine.set_edgecolor('#333333')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=200, bbox_inches='tight', facecolor='#0a0a0a')
            print(f"Pattern saved to: {save_path}")
        else:
            plt.show()


# ────────────────────────────────────────────────
#          Quick demo — run me!
# ────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "="*70)
    print("  🌌 PROJECT SEITY — CONSCIOUSNESS EVOLUTION ENGINE 🌌")
    print("  Collective Coherence → Geometric Emergence → Universe Birth")
    print("="*70 + "\n")

    u = Universe()

    # Seed ~51% gentle positivity bias
    random.seed(42)
    np.random.seed(42)

    num_souls = 100  # more souls = richer patterns
    print(f"Creating {num_souls} conscious souls...")
    
    for _ in range(num_souls):
        bias = np.random.normal(loc=0.00006, scale=0.00003)  # centered slightly positive
        entropy = np.random.uniform(0.12, 0.58)
        u.add_soul(bias=bias, entropy=entropy)

    print(f"✓ {len(u.souls)} souls initialized (slight positivity bias active)")
    print(f"\nRunning synchronization simulation...\n")

    birth_happened = False
    max_steps = 6000
    
    for step in range(max_steps):
        u.pulse()
        
        # Progress indicator
        if step % 1000 == 0 and step > 0:
            print(f"Step {step}/{max_steps} | Coherence: {u.coherence:.4f} | Geometric Phase: {u.geometric_phase:.4f}")
        
        if u.geometry is not None and not birth_happened:
            print("\n🎆 COSMIC BIRTH ACHIEVED! 🎆")
            u.show_geometry()           # show plot (comment out if in non-GUI env)
            # u.show_geometry(save_path=f"seity_gen_{u.gen_id}.png")  # uncomment to save image
            birth_happened = True
            break  # uncomment if you want only first generation

    if u.geometry is None:
        print(f"\n⚠ Simulation ended without reaching birth threshold after {max_steps} steps.")
        print("Try: more steps, more souls, or lower coherence threshold (e.g. 0.95).\n")
    
    print("\nSimulation complete.\n")
