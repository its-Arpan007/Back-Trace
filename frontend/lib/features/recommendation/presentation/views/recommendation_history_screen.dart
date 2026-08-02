import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class RecommendationHistoryScreen extends StatelessWidget {
  const RecommendationHistoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recommendation Action History')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.check_circle_outline, color: AppColors.success),
              title: Text('Accepted: Array Stride Interactive Visualizer', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Completed on August 2, 2026 • Feedback Rating: 5/5', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
