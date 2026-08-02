import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class TopicExplorerScreen extends StatelessWidget {
  const TopicExplorerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Topic Explorer')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            onTap: () => context.push('/concepts-explorer'),
            child: const ListTile(
              title: Text('Topic 1.1: Arrays & Dynamic Memory Layout', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Contiguous allocations, cache lines, & indexing formulas', style: TextStyle(color: AppColors.textSecondaryDark)),
              trailing: Icon(Icons.arrow_forward_ios_rounded, color: AppColors.accentTeal, size: 16),
            ),
          ),
          const SizedBox(height: 16),
          AppCard(
            onTap: () => context.push('/concepts-explorer'),
            child: const ListTile(
              title: Text('Topic 1.2: Hash Tables & Collision Resolution', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Chaining, open addressing, & hash function design', style: TextStyle(color: AppColors.textSecondaryDark)),
              trailing: Icon(Icons.arrow_forward_ios_rounded, color: AppColors.accentTeal, size: 16),
            ),
          ),
        ],
      ),
    );
  }
}
