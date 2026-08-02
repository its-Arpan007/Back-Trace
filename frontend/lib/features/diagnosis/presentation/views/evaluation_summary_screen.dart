import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class EvaluationSummaryScreen extends StatelessWidget {
  const EvaluationSummaryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Evaluation Summary')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: [
            AppCard(
              child: ListTile(
                leading: const Icon(Icons.cancel_outlined, color: AppColors.error, size: 36),
                title: const Text('Evaluation: Incorrect Solution', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: const Text('Score: 0.0 / 10.0 • Match: Mismatch (Provided 0x1005 vs Expected 0x1014)', style: TextStyle(color: AppColors.textSecondaryDark)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
