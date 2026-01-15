"""Test suite for Project Seity Consciousness Evolution Engine"""
import pytest
import numpy as np
from seity_consciousness_engine import Soul, Universe


class TestSoul:
    """Test Soul dataclass functionality"""
    
    def test_soul_creation(self):
        """Test creating a soul with default values"""
        soul = Soul(phase=1.5)
        assert soul.phase == 1.5
        assert soul.bias == 0.0
        assert soul.entropy == 0.3
        assert soul.geometric_signature == 0.0
    
    def test_soul_with_custom_values(self):
        """Test creating a soul with custom values"""
        soul = Soul(phase=2.0, bias=0.001, entropy=0.5, geometric_signature=1.2)
        assert soul.phase == 2.0
        assert soul.bias == 0.001
        assert soul.entropy == 0.5
        assert soul.geometric_signature == 1.2


class TestUniverse:
    """Test Universe class functionality"""
    
    def test_universe_initialization(self):
        """Test universe starts with correct defaults"""
        u = Universe()
        assert len(u.souls) == 0
        assert u.coherence == 0.0
        assert u.geometry is None
        assert u.gen_id == 0
        assert u.a == 0.1
        assert u.geometric_phase == 0.0
        assert u.symmetry_broken is False
    
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
    
    def test_geometric_phase_accumulation(self):
        """Test that geometric phase accumulates over time"""
        u = Universe()
        u.add_soul()
        u.add_soul()
        
        initial_phase = u.geometric_phase
        for _ in range(10):
            u.pulse()
        
        # Geometric phase should accumulate
        assert u.geometric_phase > initial_phase
    
    def test_birth_trigger_conditions(self):
        """Test that birth doesn't trigger prematurely"""
        u = Universe()
        for _ in range(5):
            u.add_soul(phase=0.0, entropy=0.5)
        
        # Run a few pulses
        for _ in range(10):
            u.pulse()
        
        # With high entropy, birth shouldn't trigger easily
        assert u.geometry is None
        assert u.gen_id == 0
        assert u.symmetry_broken is False


class TestIntegration:
    """Integration tests for the full system"""
    
    def test_small_simulation(self):
        """Test a small simulation runs without errors"""
        u = Universe()
        
        # Add a small number of souls
        for _ in range(10):
            u.add_soul(bias=0.0001, entropy=0.2)
        
        # Run simulation for a few steps
        for _ in range(100):
            u.pulse()
            if u.geometry is not None:
                break
        
        # Verify universe state is valid
        assert len(u.souls) == 10
        assert 0 <= u.coherence <= 1
        assert u.geometric_phase >= 0
    
    def test_coherence_bounds(self):
        """Test that coherence stays within valid bounds"""
        u = Universe()
        for _ in range(20):
            u.add_soul()
        
        for _ in range(50):
            u.pulse()
            assert 0 <= u.coherence <= 1, f"Coherence {u.coherence} out of bounds"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
