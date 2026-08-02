import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminCurriculumManagementScreen extends StatelessWidget {
  const AdminCurriculumManagementScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Curriculum CMS Explorer')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.menu_book_rounded, color: AppColors.accentTeal),
              title: Text('Data Structures & Algorithms', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Chapters: 4 • Topics: 12 • Concepts: 42 • Bloom Levels: Aligned', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
