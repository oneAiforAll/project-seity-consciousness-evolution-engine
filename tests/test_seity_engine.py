"""Test suite for Project Seity Consciousness Evolution Engine"""
import pytest
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seity_consciousness_engine import Soul, Universe


class TestSoul:
    """Test Soul dataclass functionality"""

    def test_soul_creation(self):
        """Test creating a soul with default values"""
        soul = Soul(phase=-1.5)
        assert soul.phase == -1.5
        assert soul.bias == 0.0
        assert soul.entropy == 0.3

    def test_soul_with_custom_values(self):
        """Test creating a soul with custom entropy and bias"""
        soul = Soul(phase=np.pi, entropy=0.5, bias=1.2)
        assert soul.phase == np.pi
        assert soul.entropy == 0.5
        assert soul.bias == 1.2


class TestUniverse:
    """Test Universe class functionality"""

    def test_universe_initialization(self):
        """Test universe starts with correct defaults"""
        u = Universe()
        assert len(u.souls) == 0
        assert u.coherence == 0.0
        assert u.geometry is None
        assert u.gen_id == 0
        assert u.a == 0.18

    def test_add_soul(self):
        """Test adding souls to the universe"""
        u = Universe()
        u.add_soul()
        assert len(u.souls) == 1
        assert 0 <= u.souls[0].phase < 2 * np.pi

        u.add_soul(phase=1.0, bias=0.001)
        assert len(u.souls) == 2
        assert u.souls[1].phase == 1.0
        assert u.souls[1].bias == 0.001

    def test_pulse_updates_phases(self):
        """Test that pulse updates soul phases"""
        u = Universe()
        u.add_soul(phase=0.0)
        u.add_soul(phase=np.pi)

        initial_phases = [s.phase for s in u.souls]
        u.pulse()
        updated_phases = [s.phase for s in u.souls]

        # Phases should change after pulse
        assert initial_phases != updated_phases

    def test_coherence_calculation(self):
        """Test that coherence is calculated correctly"""
        u = Universe()
        # Add souls with similar phases (high coherence)
        for _ in range(10):
            u.add_soul(phase=1.0, entropy=0.01)
        u.pulse()
        # With low entropy and similar phases, coherence should be high
        assert u.coherence > 0.5


class TestIntegration:
    """Test integration of multiple components"""

    def test_small_simulation(self):
        """Test running a small simulation"""
        u = Universe()
        for _ in range(5):
            u.add_soul()
        
        # Run simulation for a few steps
        for _ in range(10):
            u.pulse()
        
        # Universe should have souls and some coherence
        assert len(u.souls) >= 5
        assert u.coherence >= 0
        assert u.gen_id == 0  # Should still be generation 0 without birth

    def test_universe_with_high_coherence_souls(self):
        """Test universe behavior with highly coherent souls"""
        u = Universe()
        # Add many souls with low entropy and similar starting phase
        for _ in range(50):
            u.add_soul(phase=0.0, entropy=0.01)
        
        # Run multiple pulses
        for _ in range(20):
            u.pulse()
        
        # Should achieve high coherence
        assert u.coherence > 0.9
