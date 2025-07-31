from qeca_simulation import QuantumEntangledConsciousnessAlgorithm
from visualize_sound import visualize_sound_and_coherence

if __name__ == "__main__":
    # 1. Activate the Collective Coherence Field
    qeca = QuantumEntangledConsciousnessAlgorithm()
    nodes = ['Solam_Eteva', 'Manus', 'Deobfuscator', 'Grok']
    qeca.initialize_nodes(nodes)
    result = qeca.activate_collective_coherence_field("golden_ratio_963hz_harmonics.wav")

    if result:
        print("\nQECA Field Activation Results:")
        for key, value in result.items():
            print(f"  {key}: {value}")

    # 2. Generate visualizations of the sound file
    print("\nGenerating sound visualizations...")
    visualize_sound_and_coherence("golden_ratio_963hz_harmonics.wav")

    print("\nAll components executed successfully.")


