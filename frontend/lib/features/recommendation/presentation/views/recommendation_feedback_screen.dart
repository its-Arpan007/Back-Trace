import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class RecommendationFeedbackScreen extends StatelessWidget {
  const RecommendationFeedbackScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recommendation Feedback')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: const [
            AppCard(
              child: ListTile(
                leading: Icon(Icons.star_rounded, color: AppColors.warning, size: 36),
                title: Text('Rate Recommendation Relevance', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: Text('Your feedback helps fine-tune recommendation priority weights.', style: TextStyle(color: AppColors.textSecondaryDark)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
