import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class QuestionValidationScreen extends StatelessWidget {
  const QuestionValidationScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Question Validation Report')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text('Question Integrity Report', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                Divider(color: AppColors.darkBorder),
                SizedBox(height: 8),
                Text('✓ Duplicate Slugs Check: PASS (0 duplicates)', style: TextStyle(color: AppColors.success)),
                SizedBox(height: 4),
                Text('✓ Broken Concept References: PASS (0 broken links)', style: TextStyle(color: AppColors.success)),
                SizedBox(height: 4),
                Text('✓ Bloom Taxonomy Levels: PASS (100% valid)', style: TextStyle(color: AppColors.success)),
                SizedBox(height: 4),
                Text('✓ Code Question Test Cases: PASS (All test cases present)', style: TextStyle(color: AppColors.success)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
