import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class CurriculumImportStatusScreen extends StatelessWidget {
  const CurriculumImportStatusScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Curriculum JSON Importer')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Domain Package Importer',
              style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white),
            ),
            const SizedBox(height: 8),
            const Text(
              'Import concepts.json, graph.json, questions.json, and resources.json packages.',
              style: TextStyle(color: AppColors.textSecondaryDark),
            ),
            const SizedBox(height: 24),
            AppCard(
              child: ListTile(
                leading: const Icon(Icons.check_circle_outline, color: AppColors.success, size: 36),
                title: const Text('DSA Domain Package (v1.0.0)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: const Text('Status: Validated & Imported • 4 Concepts, 4 Edges', style: TextStyle(color: AppColors.textSecondaryDark)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
