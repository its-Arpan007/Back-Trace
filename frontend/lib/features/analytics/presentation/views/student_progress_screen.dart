import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class StudentProgressScreen extends StatelessWidget {
  const StudentProgressScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Student Learning Progress')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.trending_up_rounded, color: AppColors.success, size: 36),
              title: Text('Overall Learning Progress: 78.5%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Mastered Concepts: 1 • In Progress: 3 • Total Study Time: 240 mins', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
