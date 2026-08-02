import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class QuestionImportScreen extends StatelessWidget {
  const QuestionImportScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Question Package Importer')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Import questions.json', style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white)),
            const SizedBox(height: 8),
            const Text('Upload question packages containing questions, rubrics, test cases, and resources.', style: TextStyle(color: AppColors.textSecondaryDark)),
            const SizedBox(height: 24),
            AppCard(
              child: ListTile(
                leading: const Icon(Icons.check_circle_outline, color: AppColors.success, size: 36),
                title: const Text('DSA Question Set (v1.0.0)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: const Text('2 Questions, 2 Test Cases, 2 Misconceptions Imported', style: TextStyle(color: AppColors.textSecondaryDark)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
