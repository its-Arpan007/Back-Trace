import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class TodaysLearningPlanScreen extends StatelessWidget {
  const TodaysLearningPlanScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Today's Personalized Learning Plan")),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.check_circle_outline, color: AppColors.accentTeal),
              title: Text('Task 1: Review Array Stride Concept (15 mins)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Resource: Interactive Visualizer • Outcome: Resolve Offset Gap', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
          SizedBox(height: 12),
          AppCard(
            child: ListTile(
              leading: Icon(Icons.radio_button_unchecked, color: AppColors.warning),
              title: Text('Task 2: Solve 3 Adaptive Array Questions (20 mins)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Question Set: DSA_ARRAYS_01 Practice • Target Mastery: >85%', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
          SizedBox(height: 12),
          AppCard(
            child: ListTile(
              leading: Icon(Icons.radio_button_unchecked, color: AppColors.textSecondaryDark),
              title: Text('Task 3: Spaced Revision - Tree Traversals (10 mins)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Review Queue: Prevents decay of BST traversal concept', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
