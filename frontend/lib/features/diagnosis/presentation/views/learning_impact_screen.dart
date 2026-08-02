import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class LearningImpactScreen extends StatelessWidget {
  const LearningImpactScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Mastery Learning Impact')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: const [
            AppCard(
              child: ListTile(
                leading: Icon(Icons.trending_down_rounded, color: AppColors.error, size: 36),
                title: Text('Mastery Delta: -0.10', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                subtitle: Text('Concept DSA_ARRAYS_01 mastery score adjusted from 0.85 to 0.75.', style: TextStyle(color: AppColors.textSecondaryDark)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
