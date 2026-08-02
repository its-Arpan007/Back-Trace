import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class LearningHeatmapScreen extends StatelessWidget {
  const LearningHeatmapScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Knowledge Heatmap & Graph Coloring')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.grid_on_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Curriculum Node Heatmap Visualizer', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Green (Mastered): DSA_ARRAYS_01 • Yellow (In Progress): DSA_TREES_01 • Red (Weak): DSA_GRAPH_01', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
