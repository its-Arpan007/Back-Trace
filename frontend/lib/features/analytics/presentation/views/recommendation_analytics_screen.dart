import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class RecommendationAnalyticsScreen extends StatelessWidget {
  const RecommendationAnalyticsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recommendation Effectiveness Analytics')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.thumb_up_rounded, color: AppColors.accentTeal),
              title: Text('Recommendation Acceptance Rate: 88%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Completion Rate: 82% • Avg Improvement Delta: +18%', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
