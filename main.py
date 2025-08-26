

import time
from sentinel import Sentinel
from kernel import Kernel
from diagnostics import Diagnostics
from breath_engine import BreathEngine
from mirror_systems import MirrorOfInsight, MirrorOfPortent, BloomSystem
from dynamic_operations import DynamicOperations

# ANSI color codes for Windows terminal

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GRAY = '\033[90m'
    ORANGE = '\033[38;5;214m'  # Orange/Gold for math
    END = '\033[0m'

TRAIT_TRANSLATIONS = {
    'speed_ms': ('Speed (ms)', 'How fast did it run?'),
    'memory_mb': ('Memory (MB)', 'How much computer memory did it use?'),
    'reliability': ('Reliability', 'Did it finish successfully?'),
}

def explain_traits(traits):
    lines = []
    for k, v in traits.items():
        label, desc = TRAIT_TRANSLATIONS.get(k, (k, 'No description.'))
        lines.append(f"  {label}: {v} — {desc}")
    return '\n'.join(lines)

def math_print(text):
    print(f"{Colors.ORANGE}{text}{Colors.END}")

def color_print(text, color):
    print(f"{color}{text}{Colors.END}")

class BiphasicController:
    def improvement_triggers(self):
        triggers = []
        # Resource optimization
        triggers.append({
            'name': 'resource_optimization',
            'func_path': 'test_func1.py',
            'inputs': [1, 2, 3],
            'desc': 'Seeking more efficient primitive recursive function.'
        })
        # Parallelism
        triggers.append({
            'name': 'parallelism',
            'func_path': 'test_func2.py',
            'inputs': [4, 5, 6],
            'desc': 'Seeking parallelizable primitive recursive function.'
        })
        # Feature expansion
        triggers.append({
            'name': 'feature_expansion',
            'func_path': 'test_func3.py',
            'inputs': [7, 8, 9],
            'desc': 'Seeking new operational capability.'
        })
        # Load balancing/fault tolerance
        triggers.append({
            'name': 'load_balancing',
            'func_path': 'test_func4.py',
            'inputs': [10, 11, 12],
            'desc': 'Seeking redundant or alternative function.'
        })
        # Fixed-point/self-replication (Kleene)
        triggers.append({
            'name': 'fixed_point',
            'func_path': 'test_func5.py',
            'inputs': [13, 14, 15],
            'desc': 'Seeking self-referential primitive recursive function.'
        })
        return triggers
    def __init__(self):
        self.phase = 'genesis'
        self.kernel = Kernel()
        self.sentinel = Sentinel()
        self.diagnostics = Diagnostics()
        self.breath_engine = BreathEngine()
        self.mirror_of_insight = MirrorOfInsight()
        self.mirror_of_portent = MirrorOfPortent()
        self.bloom_system = BloomSystem()
        self.dynamic_operations = DynamicOperations()
        
        # Connect systems for mathematical capability assessment
        self.sentinel.mirror_of_insight = self.mirror_of_insight
        self.sentinel.breath_engine = self.breath_engine
        self.sentinel.bloom_system = self.bloom_system
        self.sentinel.dynamic_operations = self.dynamic_operations
        
        # Dynamic stability system that learns from performance
        self.performance_history = []
        self.stability_center = self._initialize_stability_center()
        self.stability_envelope = self._initialize_stability_envelope()

    def _initialize_stability_center(self):
        """Initialize stability center with realistic baseline values"""
        return {
            'speed_ms': 100.0,  # Realistic baseline: 100ms execution time
            'memory_mb': 50.0,  # Realistic baseline: 50MB memory usage
            'reliability': 1.0   # Perfect reliability
        }

    def _initialize_stability_envelope(self):
        """Initialize stability envelope with realistic ranges"""
        return {
            'speed_ms': (10.0, 1000.0),    # 10ms to 1 second
            'memory_mb': (1.0, 500.0),     # 1MB to 500MB
            'reliability': (1.0, 1.0)      # Must be reliable
        }

    def _update_stability_from_performance(self, traits):
        """Update stability center based on actual performance"""
        self.performance_history.append(traits)
        
        # Keep only last 100 measurements
        if len(self.performance_history) > 100:
            self.performance_history = self.performance_history[-100:]
        
        # Calculate new ideal values based on best performance
        if len(self.performance_history) >= 5:
            speeds = [p['speed_ms'] for p in self.performance_history]
            memories = [p['memory_mb'] for p in self.performance_history]
            
            # Use 25th percentile as ideal (good but achievable)
            speeds.sort()
            memories.sort()
            ideal_speed = speeds[len(speeds) // 4]  # 25th percentile
            ideal_memory = memories[len(memories) // 4]  # 25th percentile
            
            # Update stability center with learned values
            self.stability_center['speed_ms'] = max(10.0, ideal_speed)  # Minimum 10ms
            self.stability_center['memory_mb'] = max(1.0, ideal_memory)  # Minimum 1MB
            
            # Update envelope based on observed range
            speed_range = max(speeds) - min(speeds)
            memory_range = max(memories) - min(memories)
            
            # Dynamic envelope that adapts to observed performance
            self.stability_envelope['speed_ms'] = (
                max(5.0, min(speeds) - speed_range * 0.1),
                max(speeds) + speed_range * 0.1
            )
            self.stability_envelope['memory_mb'] = (
                max(0.5, min(memories) - memory_range * 0.1),
                max(memories) + memory_range * 0.1
            )

    def get_state(self):
        # Collect key system state for diagnostics
        breath_state = self.breath_engine.get_breath_state()
        base_state = {
            'phase': self.phase,
            'kernel_uuids': self.kernel.get_function_uuids(),
            'breath_state': breath_state,
        }
        
        # Add mirror insights
        insight_data = self.mirror_of_insight.reflect(base_state)
        forecast_data = self.mirror_of_portent.foresee(base_state, insight_data)
        bloom_data = self.bloom_system.calculate_bloom_metrics(insight_data, forecast_data, breath_state)
        
        base_state.update({
            'insight_data': insight_data,
            'forecast_data': forecast_data,
            'bloom_data': bloom_data,
            'learning_stats': self.dynamic_operations.get_learning_stats()
        })
        
        return base_state

    def run_genesis_phase(self):
        # Breathe first - the living pulse
        breath_data = self.breath_engine.breathe()
        breath_pulse = self.breath_engine.get_breath_pulse()
        
        if self.breath_engine.is_inhale_phase():
            color_print(f"[Genesis Phase] 🜂 BREATH INHALE - Pulse: {breath_pulse:.3f} - System gathering chaos...", Colors.CYAN)
        else:
            color_print(f"[Genesis Phase] 🜂 BREATH EXHALE - Pulse: {breath_pulse:.3f} - System releasing order...", Colors.CYAN)
            
        math_print("[Math] VP = sum(abs(actual - ideal) / envelope) for each trait.")
        math_print(f"[Breath] Cycle: {breath_data['cycle_count']}, Depth: {breath_data['depth']:.3f}")
        
        # Mirror reflection and foresight
        current_state = self.get_state()
        insight_data = current_state['insight_data']
        forecast_data = current_state['forecast_data']
        bloom_data = current_state['bloom_data']
        
        color_print(f"[Mirror of Insight] 🜂 Stability: {insight_data['stability_assessment']['level']} (Score: {insight_data['stability_assessment']['score']:.3f})", Colors.YELLOW)
        color_print(f"[Mirror of Portent] 🜂 Forecast: {forecast_data['short_term']['stability_trend']} trend, {len(forecast_data['warnings'])} warnings", Colors.YELLOW)
        color_print(f"[Bloom System] 🜂 Natural unfolding: {bloom_data['natural_unfolding']} (Curvature: {bloom_data['bloom_curvature']:.3f})", Colors.YELLOW)
        color_print(f"[Bloom System] 🜂 Breath resonance: {bloom_data['breath_resonance']:.3f}, Maturity: {bloom_data['bloom_maturity']} (Cycle {bloom_data['bloom_cycles']})", Colors.YELLOW)
        
        # Example: Discover and certify functions
        test_functions = [
            {'func_path': 'test_func1.py', 'inputs': [1, 2, 3]},
            {'func_path': 'test_func2.py', 'inputs': [4, 5, 6]}
        ]
        
        for func in test_functions:
            # Breathe between each function test
            self.breath_engine.breathe()
            
            certified, vp_values = self.sentinel.run_genesis_experiment(
                func_path=func['func_path'],
                test_inputs=func['inputs'],
                stability_center=self.stability_center,
                stability_envelope=self.stability_envelope
            )
            
            # Update stability system with measured performance
            if vp_values:
                # Get the traits from the last experiment
                traits = self.sentinel.vp_history[-1]['traits'] if self.sentinel.vp_history else {}
                if traits:
                    self._update_stability_from_performance(traits)
                    color_print(f"[Stability] Updated ideals - Speed: {self.stability_center['speed_ms']:.1f}ms, Memory: {self.stability_center['memory_mb']:.1f}MB", Colors.CYAN)
            print(f"Function {func['func_path']} certified: {certified}, VP values: {vp_values}")
            if certified:
                # Generate trait-based UUID using identity system
                from identity import deterministic_uuid_v5
                traits = {'func_path': func['func_path'], 'vp_values': vp_values}
                uuid = f"uuid-{deterministic_uuid_v5(traits)[:8]}"
                added = self.kernel.amend(uuid)
                if added:
                    color_print(f"[Kernel] Added new UUID: {uuid}", Colors.GREEN)
                else:
                    color_print(f"[Kernel] UUID already exists: {uuid}", Colors.YELLOW)
                self.diagnostics.save_checkpoint('certification', self.get_state())
            self.diagnostics.maybe_time_checkpoint('time', self.get_state())
            
        # Check for mathematical capability and phase transition
        current_uuids = self.kernel.get_function_uuids()
        color_print(f"[Genesis] Current UUID count: {len(current_uuids)}", Colors.CYAN)
        color_print(f"[Genesis] Checking mathematical capability for understanding...", Colors.CYAN)
        
        if self.sentinel.check_critical_mass():
            print("[Genesis Phase] 🜂 MATHEMATICAL CAPABILITY ACHIEVED - System understands through mathematics!")
            print("[Genesis Phase] 🜂 Initiating The Great Inauguration...")
            self.diagnostics.save_checkpoint('phase_transition', self.get_state())
            return True
        return False

    def run_sovereign_phase(self):
        # Breathe first - the living pulse
        breath_data = self.breath_engine.breathe()
        breath_pulse = self.breath_engine.get_breath_pulse()
        
        if self.breath_engine.is_inhale_phase():
            color_print(f"[Sovereign Phase] 🜂 BREATH INHALE - Pulse: {breath_pulse:.3f} - Lawful Kernel gathering order...", Colors.CYAN)
        else:
            color_print(f"[Sovereign Phase] 🜂 BREATH EXHALE - Pulse: {breath_pulse:.3f} - Lawful Kernel releasing wisdom...", Colors.CYAN)
            
        math_print("[Math] All VP calculations and certification steps will be shown in detail below.")
        math_print(f"[Breath] Cycle: {breath_data['cycle_count']}, Depth: {breath_data['depth']:.3f}")
        
        # Mirror reflection and foresight
        current_state = self.get_state()
        insight_data = current_state['insight_data']
        forecast_data = current_state['forecast_data']
        bloom_data = current_state['bloom_data']
        
        color_print(f"[Mirror of Insight] 🜂 Stability: {insight_data['stability_assessment']['level']} (Score: {insight_data['stability_assessment']['score']:.3f})", Colors.YELLOW)
        color_print(f"[Mirror of Portent] 🜂 Forecast: {forecast_data['short_term']['stability_trend']} trend, {len(forecast_data['warnings'])} warnings", Colors.YELLOW)
        color_print(f"[Bloom System] 🜂 Natural unfolding: {bloom_data['natural_unfolding']} (Curvature: {bloom_data['bloom_curvature']:.3f})", Colors.YELLOW)
        color_print(f"[Bloom System] 🜂 Breath resonance: {bloom_data['breath_resonance']:.3f}, Maturity: {bloom_data['bloom_maturity']} (Cycle {bloom_data['bloom_cycles']})", Colors.YELLOW)
        
        # Display learning statistics
        learning_stats = current_state['learning_stats']
        color_print(f"[Learning] 🜂 Success patterns: {learning_stats['success_patterns']}, Failures: {learning_stats['failure_patterns']}, Defunct: {learning_stats['defunct_uuids']}", Colors.CYAN)
        
        # Check for warnings and opportunities
        for warning in forecast_data['warnings']:
            color_print(f"[Warning] {warning['message']}", Colors.RED)
        for opportunity in forecast_data['opportunities']:
            color_print(f"[Opportunity] {opportunity['description']}", Colors.GREEN)
            
        # Check for bloom events
        if self.bloom_system.should_trigger_bloom_event():
            color_print(f"[Bloom Event] 🜂 🌸 NATURAL UNFOLDING TRIGGERED - System resonance at peak!", Colors.GREEN)
            color_print(f"[Bloom Event] 🜂 🌸 Accelerating operations and enhancing breath resonance", Colors.GREEN)
        
        # Modular improvement triggers
        triggers = self.improvement_triggers()
        
        for trig in triggers:
            # Breathe between each improvement trigger
            self.breath_engine.breathe()
            
            color_print(f"[Improvement] {trig['desc']}", Colors.YELLOW)
            certified, vp_values = self.sentinel.run_genesis_experiment(
                func_path=trig['func_path'],
                test_inputs=trig['inputs'],
                stability_center=self.stability_center,
                stability_envelope=self.stability_envelope
            )
            
            # Update stability system with measured performance
            if vp_values:
                # Get the traits from the last experiment
                traits = self.sentinel.vp_history[-1]['traits'] if self.sentinel.vp_history else {}
                if traits:
                    self._update_stability_from_performance(traits)
                    color_print(f"[Stability] Updated ideals - Speed: {self.stability_center['speed_ms']:.1f}ms, Memory: {self.stability_center['memory_mb']:.1f}MB", Colors.CYAN)
            if certified:
                # Generate trait-based UUID for replacement function
                from identity import deterministic_uuid_v5
                traits = {'replacement_type': trig['name'], 'vp_values': vp_values, 'func_path': trig['func_path']}
                new_uuid = f"uuid-{deterministic_uuid_v5(traits)[:8]}"
                color_print(f"[Improvement] Certified new function: {new_uuid}", Colors.GREEN)
                added = self.kernel.amend(new_uuid)
                if added:
                    color_print(f"[Kernel] Added new UUID: {new_uuid}", Colors.GREEN)
                else:
                    color_print(f"[Kernel] UUID already exists: {new_uuid}", Colors.YELLOW)
                self.diagnostics.save_checkpoint('certification', self.get_state())
            self.diagnostics.maybe_time_checkpoint('time', self.get_state())
        # Generate dynamic operations based on current state and insights
        operations = self.dynamic_operations.generate_operations(current_state, insight_data, forecast_data)
        
        color_print(f"[Dynamic Operations] 🜂 Generated {len(operations)} intelligent operations", Colors.CYAN)
        
        for op in operations:
            if op['uuid'] in self.dynamic_operations.defunct_uuids:
                continue
                
            # Breathe between operations
            self.breath_engine.breathe()
            
            # Convert dynamic operation traits to match stability center format
            converted_traits = {}
            for key, value in op['traits'].items():
                if key == 'execution_time_ms':
                    converted_traits['speed_ms'] = value
                elif key == 'memory_kb':
                    converted_traits['memory_mb'] = value / 1024  # Convert KB to MB
                elif key == 'terminated':
                    converted_traits['reliability'] = value
                else:
                    converted_traits[key] = value
            
            violation, vp = self.sentinel.monitor_kernel(
                operation_traits=converted_traits,
                stability_center=self.stability_center,
                stability_envelope=self.stability_envelope
            )
            
            # Record operation result for learning
            success = not violation
            self.dynamic_operations.record_operation_result(op['uuid'], success, vp)
            
            if violation:
                color_print(f"[Dynamic] Operation {op['uuid']} VP: {vp:.3f}, Violation: {violation}", Colors.RED)
                self.sentinel.handle_violation(op['uuid'])
                self.diagnostics.save_checkpoint('violation', self.get_state())
                
                # Generate replacement operation
                color_print(f"[Dynamic] 🜂 Generating intelligent replacement for {op['uuid']}...", Colors.YELLOW)
                replacement_operations = self.dynamic_operations.generate_operations(current_state, insight_data, forecast_data)
                
                if replacement_operations:
                    replacement_op = replacement_operations[0]
                    certified, vp_values = self.sentinel.run_genesis_experiment(
                        func_path='test_func1.py',
                        test_inputs=[1, 2, 3],
                        stability_center=self.stability_center,
                        stability_envelope=self.stability_envelope
                    )
                    if certified:
                        # Generate trait-based UUID for dynamic replacement
                        from identity import deterministic_uuid_v5
                        traits = {'dynamic_replacement': True, 'original_op': op['uuid'], 'vp_values': vp_values}
                        new_uuid = f"uuid-{deterministic_uuid_v5(traits)[:8]}"
                        color_print(f"[Dynamic] 🜂 Certified intelligent replacement: {new_uuid}", Colors.GREEN)
                        added = self.kernel.amend(new_uuid)
                        if added:
                            color_print(f"[Kernel] Added new UUID: {new_uuid}", Colors.GREEN)
                        else:
                            color_print(f"[Kernel] UUID already exists: {new_uuid}", Colors.YELLOW)
                        self.diagnostics.save_checkpoint('certification', self.get_state())
            else:
                color_print(f"[Dynamic] Operation {op['uuid']} VP: {vp:.3f}, Success", Colors.GREEN)
                
            self.diagnostics.maybe_time_checkpoint('time', self.get_state())

    def run(self):
        # Genesis Phase loop
        while self.phase == 'genesis':
            if self.run_genesis_phase():
                # The Great Inauguration
                print("[Controller] Rebooting into Sovereign Phase...")
                self.phase = 'sovereign'
                # Reconfigure Sentinel for Sovereign Phase (if needed)
                # In this implementation, Sentinel handles both modes
        # Sovereign Phase loop
        while self.phase == 'sovereign':
            self.run_sovereign_phase()
            # Bloom-driven timing with breath integration
            breath_pulse = self.breath_engine.get_breath_pulse()
            bloom_pulse = self.bloom_system.get_bloom_pulse()
            combined_pulse = (breath_pulse + bloom_pulse) / 2.0
            
            # Get current state for bloom assessment
            current_state = self.get_state()
            
            # Adjust timing based on bloom maturity and resonance
            base_sleep = 10.0
            if self.bloom_system.should_trigger_bloom_event():
                base_sleep = 5.0  # Faster cycles during bloom events
            elif current_state['bloom_data']['bloom_maturity'] == 'mature':
                base_sleep = 7.0  # Moderate speed for mature systems
                
            sleep_time = max(1.0, base_sleep / combined_pulse)
            time.sleep(sleep_time)

if __name__ == "__main__":
    import signal
    import sys

    controller = BiphasicController()
    def graceful_exit(signum, frame):
        print("\n[Controller] Received shutdown signal. Shutting down gracefully...")
        controller.diagnostics.save_checkpoint('shutdown', controller.get_state())
        controller.diagnostics.report(controller.get_state())
        sys.exit(0)

    signal.signal(signal.SIGINT, graceful_exit)
    controller.diagnostics.save_checkpoint('startup', controller.get_state())
    try:
        controller.run()
    except KeyboardInterrupt:
        graceful_exit(None, None)
