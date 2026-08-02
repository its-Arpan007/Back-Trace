import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ReviewScheduleScreen extends StatelessWidget {
  const ReviewScheduleScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Review Calendar & Schedule')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.event_note_rounded, color: AppColors.accentTeal),
              title: Text('Scheduled Review: DSA_ARRAYS_01', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Date: August 5, 2026 • Goal: Maintain >85% retention', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
