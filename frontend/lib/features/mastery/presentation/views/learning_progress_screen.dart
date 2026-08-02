import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class LearningProgressScreen extends StatelessWidget {
  const LearningProgressScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Learning Progress & Velocity')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.speed_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Learning Speed: 1.45x', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Concept Acquisition Rate: 2.5 concepts / week • Improvement Rate: +15%', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
