'''
Code modified by the authors of the paper: "Low-rank Subspaces for Unsupervised Entity Linking" to enable working with "Wikidata" instead of "Freebase"
'''
import argparse

sup_train=False

MAX_POS = 10
MAX_N_POSS_TEST = 100
MAX_N_POSS_TRAIN = 100
N_NEGS = 10
SAMPLE_NEGS = True
TYPE_OPT = 'mean'

parser = argparse.ArgumentParser()
parser.add_argument("--mode", type=str, help="train or eval", default='train')
parser.add_argument("--model_path", type=str, help="model path to save/load", default='model')
parser.add_argument("--n_epochs", type=int, help="number of epochs", default=20 if not sup_train else 50)
parser.add_argument("--batchsize", type=int, help="batchsize", default=50)
parser.add_argument("--max_len", type=int, help="max sentence length", default=100)

parser.add_argument("--lr", type=float, help="learning rate", default=1e-3)
parser.add_argument("--dropout", type=float, help="dropout rate", default=0)
parser.add_argument("--lstm_hiddim", type=int, help="hiddim of the encoder's combine", default=100)
parser.add_argument("--enc_type", type=str, default="lstm")
parser.add_argument("--n_filters", type=int, default=200)
parser.add_argument("--en_dim", type=int, default = 300)
parser.add_argument("--pos_embdim", type=int, default=5)
parser.add_argument("--type_embdim", type=int, default=50)
parser.add_argument("--ent_embdim", type=int, default=100)

parser.add_argument("--datadir", type=str, default='data/wikidata/')
parser.add_argument("--noise_threshold", type=float, default=0.75 if not sup_train else 1)
parser.add_argument("--margin", type=float, default=0.1)
parser.add_argument("--kl_coef", type=float, default=5 if not sup_train else 0)
parser.add_argument("--noise_prior", type=float, default=0.9)
parser.add_argument("--train_data", type=str, default='data/el_annotated_170k_le_titov.json')
parser.add_argument("--dev_data", type=str, default='data/aida_testa_le_titov.json')
parser.add_argument("--test_data", type=str, default='data/aida_testb_le_titov.json')
